from django.core.urlresolvers import reverse

from .mixins import VideoListMixin, VideoDetailMixin, VideoUserListMixin
from .mixins import VideoByTagListMixin, TagListMixin, VideoEditMixin
from .forms import VideoEdit


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


class VideoEdit(VideoEditMixin):
    template_name = 'videos/video_edit.html'
    form_class = VideoEdit

    def get_success_url(self):
        return reverse('web:videos:video_edit', args=[self.kwargs['pk']])
