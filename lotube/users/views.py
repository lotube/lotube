from django.views.generic import View, ListView, CreateView

from .models import User


class UserList(ListView):
    model = User
    template_name = 'users/user_list.html'
