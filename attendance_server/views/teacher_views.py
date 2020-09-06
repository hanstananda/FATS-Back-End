# Create your views here.
from rest_framework import viewsets, generics, permissions
from rest_framework.response import Response

from attendance_server import permissions as custom_permissions
from attendance_server.models import *
from attendance_server.serializers import *


class CourseClassReadViewSet(viewsets.ReadOnlyModelViewSet):
    """
        API endpoint that allows course classes to be viewed.
    """
    # TODO: Add permission check to only able to list/retrieve courses taught by teacher invoking the request
    queryset = CourseClass.objects.all()
    serializer_class = CourseClassSerializer
    permission_classes = [custom_permissions.TeacherOnly]


class CourseReadViewSet(viewsets.ReadOnlyModelViewSet):
    """
        API endpoint that allows course to be viewed.
    """
    # TODO: Add permission check to only able to list/retrieve courses taught by teacher invoking the request
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [custom_permissions.TeacherOnly]


class CourseTeacherViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows courses taught by specific teacher to be viewed.
    """
    queryset = CourseTeacher.objects.all()
    serializer_class = CourseTeacherSerializer
    permission_classes = [custom_permissions.CourseTeacherOwnerOnly, custom_permissions.TeacherOnly]

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        user = self.request.user
        teacher = TeacherProfile.objects.get(user=user)
        if user is not None:
            queryset = queryset.filter(teachers=teacher)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class CourseScheduleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows course schedules to be viewed or edited.
    """
    queryset = CourseSchedule.objects.all()
    serializer_class = CourseScheduleSerializer
    permission_classes = [custom_permissions.TeacherOnly]


class AttendanceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows attendance to be viewed or edited.
    """
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = [custom_permissions.TeacherOnly]
