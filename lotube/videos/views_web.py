from .mixins import VideoListMixin, VideoDetailMixin, VideoUserListMixin


class VideoList(VideoListMixin):
    pass


class VideoDetail(VideoDetailMixin):
    pass


class VideoUserList(VideoUserListMixin):
    pass
