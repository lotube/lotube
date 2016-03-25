from core.mixins import JSONView
from .mixins import UserListMixin, UserDetailMixin


def get_item(db_user):
    return {
        'id': db_user.id,
        'username': db_user.username,
        'first_name': db_user.first_name,
        'last_name': db_user.last_name,
        'created_at': db_user.date_joined,
        'last_login': db_user.last_login,
        'is_staff': db_user.is_staff,
        'is_active': db_user.is_active,
    }

class UserListJSON(JSONView, UserListMixin):
    """
    List of users
    """

    def craft_response(self, context, **response_kwargs):
        items = [get_item(db_user) for db_user in context['user_list']]
        response = {
            'page_info': {
                'total_results': len(items),
                'results_page': len(items),
            },
            'items': items
        }
        return response


class UserDetailJSON(JSONView, UserDetailMixin):
    """
    User details
    """

    def craft_response(self, context, **response_kwargs):
        user = context['object']
        return get_item(user)
