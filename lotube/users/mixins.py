from django.views.generic import View, ListView, CreateView, DetailView
from django.shortcuts import get_object_or_404
from django.contrib.auth import models

from .models import User


class UserListMixin(ListView):
    model = User
    template_name = 'users/user_list.html'


class UserDetailMixin(DetailView):
    model = User
    template_name = 'users/user_detail.html'

    def get_object(self):
        auth_user = get_object_or_404(models.User, username=self.kwargs['username'])
        user = get_object_or_404(self.model, user=auth_user)
        return user
