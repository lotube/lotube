from core.mixins import JSONView
from .mixins import UserListMixin, UserDetailMixin


class UserListJSON(JSONView, UserListMixin):
    """
    List of users
    """

    def craft_response(self, context, **response_kwargs):
        items = [{
            'id': db_user.user.id,
            'username': db_user.user.username,
            'first_name': db_user.user.first_name,
            'last_name': db_user.user.last_name,
            'created_at': db_user.user.date_joined,
            'last_login': db_user.user.last_login,
            'is_staff': db_user.user.is_staff,
            'is_active': db_user.user.is_active,
        } for db_user in context['user_list']]
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
        db_user = context['object']
        response = {
            'id': db_user.user.id,
            'username': db_user.user.username,
            'first_name': db_user.user.first_name,
            'last_name': db_user.user.last_name,
            'created_at': db_user.user.date_joined,
            'last_login': db_user.user.last_login,
            'is_staff': db_user.user.is_staff,
            'is_active': db_user.user.is_active,
        }
        return response
