from .mixins import VideoListMixin, VideoDetailMixin, VideoUserListMixin
from .mixins import VideoByTagListMixin


class VideoList(VideoListMixin):
    template_name = 'videos/video_list.html'


class VideoDetail(VideoDetailMixin):
    template_name = 'videos/video_detail.html'


class VideoUserList(VideoUserListMixin):
    template_name = 'videos/video_user_list.html'


class VideoByTagList(VideoByTagListMixin):
    template_name = 'videos/video_list.html'
