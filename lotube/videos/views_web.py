from .mixins import VideoListMixin, VideoDetailMixin, VideoUserListMixin
from .mixins import VideoByTagListMixin, TagListMixin


class VideoList(VideoListMixin):
    template_name = 'videos/video_list.html'
    context_object_name = 'video_list'


class VideoDetail(VideoDetailMixin):
    template_name = 'videos/video_detail.html'


class VideoUserList(VideoUserListMixin):
    template_name = 'videos/video_list.html'


class VideoByTagList(VideoByTagListMixin):
    template_name = 'videos/video_list.html'
    context_object_name = 'tag_list'


class TagList(TagListMixin):
    template_name = 'videos/tag_list.html'
