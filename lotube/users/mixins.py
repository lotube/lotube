from django.views.generic import View, ListView, CreateView

from .models import User


class UserListMixin(ListView):
    model = User
    template_name = 'users/user_list.html'
