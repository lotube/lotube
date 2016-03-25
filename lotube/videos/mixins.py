from django.views.generic import View, ListView, CreateView, DetailView

from .models import Video


class VideoListMixin(ListView):
    model = Video
    template_name = 'videos/video_list.html'


class VideoDetailMixin(DetailView):
    model = Video
    template_name = 'videos/video_detail.html'


class VideoUserListMixin(ListView):
    model = Video
    template_name = 'videos/video_user_list.html'
