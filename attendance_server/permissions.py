import logging

from rest_framework import permissions


class TeacherOwnerOnly(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        # Instance must have an attribute named `teachers`.
        if request.method in permissions.SAFE_METHODS:
            return obj.teachers.user == request.user
        return False
