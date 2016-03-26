from .mixins import UserListMixin, UserDetailMixin


class UserList(UserListMixin):
    template_name = 'users/user_list.html'


class UserDetail(UserDetailMixin):
    template_name = 'users/user_detail.html'
