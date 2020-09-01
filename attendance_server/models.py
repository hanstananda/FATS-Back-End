from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Course(models.Model):
    name = models.CharField(max_length=200)
    index = models.CharField(max_length=200, blank=True, null=True)
    type = models.CharField(max_length=200, blank=True, null=True)


class CourseSchedule(models.Model):
    name = models.ForeignKey(Course, on_delete=models.CASCADE)
    time = models.DateTimeField()
    teachers = models.ManyToManyField(User)


class Attendance(models.Model):
    course_schedule = models.ForeignKey(CourseSchedule, on_delete=models.CASCADE)
    attendee = models.ForeignKey(User, on_delete=models.CASCADE)
