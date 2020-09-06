import logging

from rest_framework import permissions

from attendance_server.models import TeacherProfile, CourseClass, CourseTeacher


class CourseTeacherOwnerOnly(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `teachers` attribute.
    """

    def has_object_permission(self, request, view, obj):
        # Instance must have an attribute named `teachers`.
        if request.method in permissions.SAFE_METHODS:
            return obj.teachers.user == request.user
        return False


class CourseClassOwnerOnly(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj: CourseClass):
        # Instance must have an attribute named `teachers`.
        if request.method in permissions.SAFE_METHODS:
            return True
        return False


class TeacherOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.user and
            request.user.is_authenticated and
            TeacherProfile.objects.filter(user=request.user).exists()
        )
