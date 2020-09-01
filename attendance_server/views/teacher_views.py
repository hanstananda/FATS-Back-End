# Create your views here.
from rest_framework import viewsets
from rest_framework.response import Response

from attendance_server import permissions
from attendance_server.models import *
from attendance_server.serializers import *


class CourseTeacherViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows courses to be viewed or edited.
    """
    queryset = CourseTeacher.objects.all()
    serializer_class = CourseTeacherSerializer
    permission_classes = [permissions.TeacherOwnerOnly]

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        queryset = queryset.filter()

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
