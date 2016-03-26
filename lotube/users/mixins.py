from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404

from .models import User


class UserListMixin(ListView):
    model = User


class UserDetailMixin(DetailView):
    model = User

    def get_object(self):
        user = get_object_or_404(self.model, username=self.kwargs['username'])
        return user
