from annoying.functions import get_object_or_None
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView

from users.models import User
from .models import Video, Tag


class VideoListMixin(ListView):
    model = Video

    def _url_params(self):
        # user params
        user = self.request.GET.get('user')
        if user:
            user = User.objects.filter(username=user)

        # video params
        video_kwargs = {}

        title = self.request.GET.get('title')
        if title:
            video_kwargs['title__contains'] = title

        tags = self.request.GET.get('tags')
        if tags:
            video_kwargs['tags'] = tags

        return video_kwargs

    def get_queryset(self):
        self._url_params()
        queryset = self.model.objects.filter(**self._url_params())
        return queryset


class VideoDetailMixin(DetailView):
    model = Video


class VideoUserListMixin(ListView):
    model = Video

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs['username'])
        queryset = self.model.objects.filter(user=user)
        return queryset


class VideoByTagListMixin(ListView):
    model = Tag

    def get_queryset(self):
        tags = self.kwargs['tags'].split(',')
        queryset = Video.objects.none()
        for tag in tags:
            tag_queryset = get_object_or_None(self.model, name=tag)
            if tag_queryset is not None:
                queryset = queryset | \
                           self.model.objects.get(name=tag).videos.all()
        return queryset.distinct()


class TagListMixin(ListView):
    model = Tag
