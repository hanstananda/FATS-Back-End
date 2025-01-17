from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions

from attendance_server.serializers import *


class UserViewSetAdmin(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]


class CourseViewSetAdmin(viewsets.ModelViewSet):
    """
    API endpoint that allows courses to be viewed or edited.
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAdminUser]


class CourseClassViewSetAdmin(viewsets.ModelViewSet):
    """
    API endpoint that allows course class to be viewed or edited.
    """
    queryset = CourseClass.objects.all()
    serializer_class = CourseClassSerializer
    permission_classes = [permissions.IsAdminUser]


class CourseScheduleViewSetAdmin(viewsets.ModelViewSet):
    """
    API endpoint that allows course schedule to be viewed or edited.
    """
    queryset = CourseSchedule.objects.all()
    serializer_class = CourseScheduleSerializer
    permission_classes = [permissions.IsAdminUser]


class AttendanceViewSetAdmin(viewsets.ModelViewSet):
    """
    API endpoint that allows course attendance to be viewed or edited.
    """
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = [permissions.IsAdminUser]


class CourseTeacherViewSetAdmin(viewsets.ModelViewSet):
    """
    API endpoint that allows teachers teaching the course to be viewed or edited.
    """
    queryset = CourseTeacher.objects.all()
    serializer_class = CourseTeacherSerializer
    permission_classes = [permissions.IsAdminUser]


class CourseStudentViewSetAdmin(viewsets.ModelViewSet):
    """
    API endpoint that allows students taking the course to be viewed or edited.
    """
    queryset = CourseStudent.objects.all()
    serializer_class = CourseStudentSerializer
    permission_classes = [permissions.IsAdminUser]