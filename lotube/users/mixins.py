from django.http import Http404
from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404
from django.views.generic.edit import DeleteView, UpdateView

from config import constants
from core.mixins import CustomLoginRequiredMixin
from .models import User


class OwnerRequiredMixin(CustomLoginRequiredMixin):

    def dispatch(self, request, **kwargs):
        if not request.user.is_authenticated()\
                or request.user.username != kwargs['username']:
            raise Http404('Not logged in or not the owner')
        return super(OwnerRequiredMixin, self).dispatch(request, **kwargs)


class UserListMixin(ListView):
    model = User
    paginate_by = constants.PAGINATE_BY


class UserDetailMixin(DetailView):
    model = User

    def get_object(self):
        user = get_object_or_404(self.model, username=self.kwargs['username'])
        return user


class UserUpdateMixin(OwnerRequiredMixin, UpdateView):
    model = User

    def get_object(self):
        user = get_object_or_404(self.model, username=self.kwargs['username'])
        return user


class UserDeleteMixin(OwnerRequiredMixin, DeleteView):
    model = User

    def get_object(self):
        user = get_object_or_404(self.model, username=self.kwargs['username'])
        return user
