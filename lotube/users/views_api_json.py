from core.mixins import JSONView
from .mixins import UserListMixin


class UserListJSON(JSONView, UserListMixin):
    """
    Returns a list of users, such as:
    [
        { "id": 1,
          "username": "tommy33",
          "first_name": "Tommy",
          "last_name": "Sun",
          "created_at": "2016-01-01"
        }, ...
    ]
    """
    def craft_response(self, context, **response_kwargs):
        items = []
        for dbuser in context['user_list']:
            user = {
                'id': dbuser.user.id,
                'username': dbuser.user.username,
                'first_name': dbuser.user.first_name,
                'last_name': dbuser.user.last_name,
                'created_at': dbuser.user.date_joined,
                'last_login': dbuser.user.last_login,
                'is_staff': dbuser.user.is_staff,
                'is_active': dbuser.user.is_active,
            }
            items.append(user)
        response = {
            'page_info': {
                'total_results': len(items),
                'results_page': len(items),
            },
            'items': items
        }
        return response
