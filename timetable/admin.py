from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Level)

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("name", "course_code", )
    list_filter = ("name", )
    search_fields = ("name", "course_code", )

@admin.register(Semester)
class SemesterAdmin(admin.ModelAdmin):
    list_display = ("name", )
    list_filter = ("name", )
    search_fields = ("name", )

@admin.register(Lecturer)
class LecturerAdmin(admin.ModelAdmin):
    list_display = ("name",)
    list_filter = ("name", )
    search_fields = ("name", "courses", "levels", "semester", )

@admin.register(Timetable)
class TimetableAdmin(admin.ModelAdmin):
    list_display = ("day", "course", "start_time", "end_time", )
    list_filter = ("day", )
    search_fields = ("day", "course", "start_time", "end_time", )

@admin.register(Curriculum)
class CurriculumAdmin(admin.ModelAdmin):
    list_display = ("level", "semester", "course", "lecturer", )
    list_filter = ("level", )
    search_fields = ("level", "semester", "course", "lecturer", )
