from django.urls import path
from .views import home_view, timetable_view, fetch_timetable, curriculum_view, lecturer_view, fetch_lecturers

urlpatterns = [
    path('', home_view, name='home'),
    path('timetable/', timetable_view, name='timetable'),
    path('fetch-timetable/', fetch_timetable, name='fetch_timetable'),
    path('curriculum/', curriculum_view, name='curriculum'),
    path('lecturers/', lecturer_view, name='lecturers'),
    path('fetch-lecturers/', fetch_lecturers, name='fetch_lecturers'),
] 
