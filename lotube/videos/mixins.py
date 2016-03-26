from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView

from users.models import User
from .models import Video


class VideoListMixin(ListView):
    model = Video


class VideoDetailMixin(DetailView):
    model = Video


class VideoUserListMixin(ListView):
    model = Video

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs['username'])
        queryset = self.model.objects.filter(user=user)
        return queryset
