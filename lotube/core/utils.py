from django.core.exceptions import PermissionDenied, ValidationError


class SerializerContextUtils(object):

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
