from django.http import JsonResponse

from .mixins import UserListMixin


class UserListJSON(UserListMixin):

    def render_to_response(self, context, **response_kwargs):
        #print context
        return JsonResponse({
            'key': 'value'
        })
