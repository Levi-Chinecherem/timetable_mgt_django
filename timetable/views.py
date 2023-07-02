from django.shortcuts import render
from .models import Course
from .models import Lecturer
from .models import Curriculum
from .models import Timetable
from django.http import JsonResponse
from django.core import serializers

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
            timetable = Timetable.objects.filter(course__level__name=level, semester=semester)
        else:
            timetable = None

        if timetable:
            timetable_data = []
            for entry in timetable:
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
                    'semester': entry.semester
                }
                timetable_data.append(entry_data)
                
            print(timetable_data)
            return JsonResponse({'success': True, 'timetable': timetable_data})
        else:
            return JsonResponse({'success': False, 'message': 'No Timetable found.'})

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
