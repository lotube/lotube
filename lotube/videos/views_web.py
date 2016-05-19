from django.core.urlresolvers import reverse
from django.views.generic import ListView

from .models import Like
from .mixins import VideoListMixin, VideoDetailMixin, VideoUserListMixin, \
    VideoCreateMixin
from .mixins import VideoByTagListMixin, TagListMixin, VideoEditMixin, \
    VideoDeleteMixin
from .forms import VideoEditForm, VideoCreateForm


class VideoList(VideoListMixin):
    template_name = 'videos/video_list.html'


class VideoDetail(VideoDetailMixin):
    template_name = 'videos/video_detail.html'


class VideoUserList(VideoUserListMixin):
    template_name = 'videos/video_list.html'


class VideoByTagList(VideoByTagListMixin):
    template_name = 'videos/video_list.html'


class TagList(TagListMixin):
    template_name = 'videos/tag_list.html'


class VideoCreate(VideoCreateMixin):
    template_name = 'videos/video_create.html'
    form_class = VideoCreateForm

    def get_success_url(self):
        return reverse('web:videos:video', args=[self.object.id])


class VideoEdit(VideoEditMixin):
    template_name = 'videos/video_edit.html'
    form_class = VideoEditForm

    def get_success_url(self):
        return reverse('web:videos:video_edit', args=[self.kwargs['pk']])


class VideoDelete(VideoDeleteMixin):
    template_name = 'videos/video_delete.html'
    success_url = '/'


class LikeList(ListView):
    template_name = 'videos/like_list.html'
    model = Like

    def get_context_data(self, **kwargs):
        context = super(LikeList, self).get_context_data()
        context['video'] = self.kwargs['pk']
        return context
