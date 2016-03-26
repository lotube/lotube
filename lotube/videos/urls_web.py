from django.conf.urls import url

from . import constants
from .views_web import VideoList, VideoDetail, VideoUserList, VideoByTagList

urlpatterns = [
    # List of Videos
    url(
        r'^$',
        VideoList.as_view(),
        name='videos'
    ),

    # Retrieve a specific Video
    url(
        r'^\/(?P<pk>\d+)$',
        VideoDetail.as_view(),
        name='video'
    ),

    # List of Videos by User
    url(
        r'^\/user/(?P<username>[\w\d]+)$',
        VideoUserList.as_view(),
        name='user_videos'
    ),

    # List of Videos by Tags
    url(
        r'^\/tags/(?P<tags>[' + constants.TAGS_ALLOWED_CHARACTERS + \
        ',]+)$',
        VideoByTagList.as_view(),
        name='videos_by_tags'
    ),
]
