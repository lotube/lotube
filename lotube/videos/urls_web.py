from django.conf.urls import url

from .views_web import VideoList, VideoDetail, VideoUserList

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
        r'^\/user\/(?P<username>[\w\d]+)$',
        VideoUserList.as_view(),
        name='user_videos'
    ),
]
