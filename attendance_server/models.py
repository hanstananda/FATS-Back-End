from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Course(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class CourseClass(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    index = models.CharField(max_length=200, blank=True, null=True)
    type = models.CharField(max_length=200)

    def __str__(self):
        res = str(self.course)
        if self.index:
            res += " index: %s" % self.index
        if self.type:
            res += " type: %s" % self.type
        return res

    class Meta:
        unique_together = ['course', 'index', 'type']


class CourseSchedule(models.Model):
    course_class = models.ForeignKey(CourseClass, on_delete=models.CASCADE)
    time = models.DateTimeField()

    def __str__(self):
        return str(self.course_class) + " at %s" % self.time.isoformat()


class Attendance(models.Model):
    course_schedule = models.ForeignKey(CourseSchedule, on_delete=models.CASCADE)
    attendee = models.ForeignKey(User, on_delete=models.CASCADE)


class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_id = models.CharField(max_length=20)
    birth_date = models.DateField(null=True, blank=True)
    face_recognition = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return str(self.user)


class TeacherProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)


class CourseTeacher(models.Model):
    course_class = models.ForeignKey(CourseClass, on_delete=models.CASCADE)
    teachers = models.ForeignKey(TeacherProfile, on_delete=models.CASCADE)

