# Create your views here.
from rest_framework import viewsets, generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

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
    serializer_class = CourseTeacherDetailedSerializer
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


class StudentProfileViewByStudentId(generics.ListAPIView):
    serializer_class = StudentProfileSerializer
    permission_classes = [custom_permissions.TeacherOnly]

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        student_id = self.request.query_params.get('student_id', '')
        return StudentProfile.objects.filter(student_id=student_id)


class OverrideAttendanceView(generics.CreateAPIView):
    serializer_class = AttendanceSerializer
    permission_classes = [custom_permissions.TeacherOnly]

    def create(self, request, *args, **kwargs):
        student_id = self.request.data['student_id']
        student = StudentProfile.objects.get(student_id=student_id).user.id
        data = dict(request.data)
        data['attendee'] = student

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)