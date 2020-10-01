# Create your views here.
import base64
import json

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
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
    serializer_class = AttendanceTeacherSerializer
    permission_classes = [custom_permissions.TeacherOnly]


class StudentProfileViewByStudentId(generics.ListAPIView):
    serializer_class = StudentProfileSerializer
    permission_classes = [custom_permissions.TeacherOnly]

    def get_queryset(self):
        """
        This view should return student profile given the student id
        """
        student_id = self.request.query_params.get('student_id', '')
        return StudentProfile.objects.filter(student_id=student_id)


class AbsentStudentView(generics.ListAPIView):
    serializer_class = StudentProfileSerializer
    permission_classes = [custom_permissions.TeacherOnly]

    def get_queryset(self):
        """
        This view should return a list of all the absent students on a given course schedule
        """
        course_schedule_id = self.request.query_params.get('course_schedule_id', '')
        course_class_id = CourseSchedule.objects.get(id=course_schedule_id).course_class_id
        # print(course_schedule_id, course_class_id)
        course_students_user_id = set(i.students.user.id for i in
                                      CourseStudent.objects.filter(course_class_id=course_class_id))
        attended_students_user_id = set(i.attendee.id for i in
                                        Attendance.objects.filter(course_schedule_id=course_schedule_id))
        # print(course_students_user_id, attended_students_user_id)
        return StudentProfile.objects.filter(user_id__in=course_students_user_id - attended_students_user_id)


class LateStudentView(generics.ListAPIView):
    serializer_class = StudentProfileSerializer
    permission_classes = [custom_permissions.TeacherOnly]

    def get_queryset(self):
        """
        This view should return a list of all the absent students on a given course schedule
        """
        course_schedule_id = self.request.query_params.get('course_schedule_id', '')
        attended_students_user_id = set(i.attendee.id for i in
                                        Attendance.objects.filter(course_schedule_id=course_schedule_id, late=True))
        return StudentProfile.objects.filter(user_id__in=attended_students_user_id)


class PresentStudentView(generics.ListAPIView):
    serializer_class = StudentProfileSerializer
    permission_classes = [custom_permissions.TeacherOnly]

    def get_queryset(self):
        """
        This view should return a list of all the absent students on a given course schedule
        """
        course_schedule_id = self.request.query_params.get('course_schedule_id', '')
        attended_students_user_id = set(i.attendee.id for i in
                                        Attendance.objects.filter(course_schedule_id=course_schedule_id, late=False))
        return StudentProfile.objects.filter(user_id__in=attended_students_user_id)


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


class StudentProfileReadViewSet(viewsets.ReadOnlyModelViewSet):
    """
        API endpoint that allows course classes to be viewed.
    """
    # TODO: Add permission check to only able to list/retrieve student taught by teacher invoking the request
    queryset = StudentProfile.objects.all()
    serializer_class = StudentProfileDetailedSerializer
    permission_classes = [custom_permissions.TeacherOnly]


@csrf_exempt
def take_attendance_by_photo(request):
    """
    Working example for encoding and format:

    import base64
    import requests
    import json
    with open("photo.jpg", "rb") as f:
        s_raw = f.read()
    s_b64 = base64.b64encode(s_raw)
    requests.post(
        url='http://localhost:8000/teacher-api/take-attendance/',
        data=json.dumps({'session_id': 123, 'raw_picture': str(s_b64, 'ascii')})
    )
    """
    serializer = TakeAttendanceSerializer(json.loads(request.body))
    photo = base64.b64decode(serializer.data['raw_picture'])
    session_id = serializer.data['session_id']

    # Store the submitted in temporary folder

    # Initialize folder of this class if not exists

    # Use deepface to detect face, return if face not detected

    # Use deepface to check photo against folder return if no face match

    # Take attendance of user in the database, return matched student id

    return HttpResponse(200)
