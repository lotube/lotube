from django.views.generic import View, ListView, CreateView, DetailView

from .models import Video


class VideoListMixin(ListView):
    model = Video
    template_name = 'videos/video_list.html'


class VideoDetailMixin(DetailView):
    model = Video
    template_name = 'videos/video_detail.html'

    #def get_object(self):
    #    auth_user = get_object_or_404(models.User, username=self.kwargs['username'])
    #    video = get_object_or_404(self.model, video=auth_user)
    #    return video
