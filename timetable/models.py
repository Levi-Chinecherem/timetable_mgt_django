from django.db import models

class Level(models.Model):
    LEVEL_CHOICES = [
        ('ND1', 'ND1'),
        ('ND2', 'ND2'),
        ('HND1', 'HND1'),
        ('HND2', 'HND2'),
    ]

    name = models.CharField(max_length=10, choices=LEVEL_CHOICES, default='ND1')

    def __str__(self) -> str:
        return f"Level: { self.name }"
    
class Course(models.Model):
    name = models.CharField(max_length=100)
    course_code = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"Course: { self.course_code }"
        

class Semester(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return f"Semester: { self.name }"
    
class Lecturer(models.Model):
    name = models.CharField(max_length=100)
    courses = models.ManyToManyField(Course)
    levels = models.ManyToManyField(Level)
    semesters = models.ManyToManyField(Semester)

    def __str__(self) -> str:
        return f"Lecturer: { self.name }"

class Timetable(models.Model):
    DAY_CHOICES = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
    ]

    SEMESTER_CHOICES = [
        ('Semester 1', 'Semester 1'),
        ('Semester 2', 'Semester 2'),
    ]

    BREAK_TIME = '12:00'

    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    lecturer = models.ForeignKey(Lecturer, on_delete=models.CASCADE)
    day = models.CharField(max_length=10, choices=DAY_CHOICES)
    start_time = models.TimeField()
    end_time = models.TimeField()
    semester = models.CharField(max_length=20, choices=SEMESTER_CHOICES)

    def __str__(self) -> str:
        return f"Timetable: { self.day } - { self.course } - { self.semester }"

class Curriculum(models.Model):
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    lecturer = models.ForeignKey(Lecturer, on_delete=models.CASCADE)
    topic_1 = models.CharField(max_length=100, blank=True)
    detail_1 = models.CharField(max_length=100, blank=True)
    topic_2 = models.CharField(max_length=100, blank=True)
    detail_2 = models.CharField(max_length=100, blank=True)
    topic_3 = models.CharField(max_length=100, blank=True)
    detail_3 = models.CharField(max_length=100, blank=True)
    topic_4 = models.CharField(max_length=100, blank=True)
    detail_4 = models.CharField(max_length=100, blank=True)
    topic_5 = models.CharField(max_length=100, blank=True)
    detail_5 = models.CharField(max_length=100, blank=True)
    topic_6 = models.CharField(max_length=100, blank=True)
    detail_6 = models.CharField(max_length=100, blank=True)
    topic_7 = models.CharField(max_length=100, blank=True)
    detail_7 = models.CharField(max_length=100, blank=True)
    topic_8 = models.CharField(max_length=100, blank=True)
    detail_8 = models.CharField(max_length=100, blank=True)
    topic_9 = models.CharField(max_length=100, blank=True)
    detail_9 = models.CharField(max_length=100, blank=True)
    topic_10 = models.CharField(max_length=100, blank=True)
    detail_10 = models.CharField(max_length=100, blank=True)

    def __str__(self) -> str:
        return f"Curriculum for: { self.level } - { self.semester } - { self.course }"
