from django.shortcuts import render
from django.db.models import F
from .models import Course
from .models import Lecturer
from .models import Curriculum
from .models import Timetable
from django.http import JsonResponse
from django.core import serializers
from django.core.exceptions import ObjectDoesNotExist


# index/home view
def home_view(request):
    return render(request, 'index.html')

# time table
def timetable_view(request):
    return render(request, 'timetable.html')


def fetch_timetable(request):
    if request.method == 'GET' and request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        level = request.GET.get('level')
        semester = request.GET.get('semester')

        if level and semester:
            timetable_entries = Timetable.objects.filter(level__name=level, semester__name=semester).order_by('start_time')
            timetable_data = []

            # Group the timetable entries by day
            days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
            grouped_entries = {day: [] for day in days}

            for entry in timetable_entries:
                grouped_entries[entry.day].append(entry)

            # Iterate over the days in the specified order and add the entries to the timetable_data
            for day in days:
                entries = grouped_entries[day]

                # Sort the entries for each day by start_time
                entries.sort(key=lambda x: x.start_time)

                if entries:
                    has_course = any(entry.course.name != 'Break Time' for entry in entries)

                    if has_course:
                        break_added = False

                        for entry in entries:
                            if entry.course.name == 'Break Time' and break_added:
                                continue  # Skip adding additional break entries

                            if entry.course.name == 'Break Time':
                                break_added = True

                            entry_data = {
                                'day': entry.day,
                                'start_time': entry.start_time.strftime('%H:%M'),
                                'end_time': entry.end_time.strftime('%H:%M'),
                                'course': {
                                    'name': entry.course.name
                                },
                                'lecturer': {
                                    'name': entry.lecturer.name
                                },
                                'semester': entry.semester.name
                            }

                            timetable_data.append(entry_data)
                    else:
                        # Remove the break time entry if there are no courses for the day
                        entries = [entry for entry in entries if entry.course.name != 'Break Time']

                        if entries:
                            break_entry_data = {
                                'day': entries[0].day,
                                'start_time': '12:00',
                                'end_time': '12:00',
                                'course': {
                                    'name': 'Break Time'
                                },
                                'lecturer': {
                                    'name': ''
                                },
                                'semester': entries[0].semester.name
                            }

                            timetable_data.append(break_entry_data)

            if timetable_data:
                return JsonResponse({'success': True, 'timetable': timetable_data})
            else:
                return JsonResponse({'success': False, 'message': 'No timetable found.'})
        else:
            return JsonResponse({'success': False, 'message': 'Invalid parameters.'})
    else:
        return render(request, 'timetable.html')



# curriculum view
def curriculum_view(request):
    if request.method == 'GET' and request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        level = request.GET.get('level')
        semester = request.GET.get('semester')
        course = request.GET.get('course')

        if level and semester and course:
            curriculum = Curriculum.objects.filter(level__name=level, semester__name=semester, course__course_code=course).first()
        else:
            curriculum = None

        if curriculum:
            data = {
                'level': curriculum.level.name,
                'semester': curriculum.semester.name,
                'course': curriculum.course.course_code,
                'topics': []
            }

            for i in range(1, 11):
                topic = getattr(curriculum, f'topic_{i}', None)
                detail = getattr(curriculum, f'detail_{i}', None)
                if topic and detail:
                    data['topics'].append({'topic': topic, 'detail': detail})

            return JsonResponse({'success': True, 'data': data})
        else:
            return JsonResponse({'success': False, 'message': 'No curriculum found.'})

    courses = Course.objects.all()

    context = {
        'courses': courses,
    }
    return render(request, 'curriculum.html', context)


# lecturers
def lecturer_view(request):
    return render(request, 'lecturers.html')

def fetch_lecturers(request):
    if request.method == 'GET' and request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        level = request.GET.get('level')
        semester = request.GET.get('semester')

        lecturers = Lecturer.objects.filter(levels__name=level, semesters__name=semester)
        lecturer_names = [lecturer.name for lecturer in lecturers]

        return JsonResponse({'lecturers': lecturer_names})
    else:
        return render(request, 'lecturers.html')
