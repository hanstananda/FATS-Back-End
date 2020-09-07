from django.contrib import admin

# Register your models here.
from attendance_server.models import *

admin.site.register(Course)
admin.site.register(CourseClass)
admin.site.register(CourseSchedule)
admin.site.register(Attendance)
admin.site.register(StudentProfile)
admin.site.register(TeacherProfile)
admin.site.register(CourseTeacher)
admin.site.register(CourseStudent)
