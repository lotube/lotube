from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404

from config import constants
from .models import User


class UserListMixin(ListView):
    model = User
    paginate_by = constants.PAGINATE_BY


class UserDetailMixin(DetailView):
    model = User

    def get_object(self):
        user = get_object_or_404(self.model, username=self.kwargs['username'])
        return user
