# Create your views here.
from rest_framework import viewsets

from attendance_server import permissions
from attendance_server.models import *
from attendance_server.serializers import *


class CourseTeacherViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows courses to be viewed or edited.
    """
    queryset = CourseTeacher.objects.all()
    serializer_class = CourseTeacherSerializer
    # permission_classes = [permissions.TeacherOwnerOnly]

