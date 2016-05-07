from django.core.exceptions import PermissionDenied, ValidationError
from rest_framework import permissions


class ContextUtils(object):

    def __init__(self, context):
        self.context = context
        self.request = context.get('request')

    def _validate_request(self):
        if not self.request:
            raise ValidationError('Context Request not found')

    def logged_in_user(self):
        self._validate_request()
        if not hasattr(self.request, "user"):
            raise PermissionDenied
        return self.request.user

    def build_absolute_uri(self, relative_uri):
        self._validate_request()
        return self.request.build_absolute_uri(relative_uri)


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow owners of a video to edit it.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user == obj.user


class IsOwnerOrReadOnlyUser(permissions.BasePermission):
    """
    Object-level permission to only allow users to edit them.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user == obj
