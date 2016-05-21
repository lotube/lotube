from django.conf.urls import include, url

from . import constants
from .views_web import VideoList, VideoDetail, VideoUserList, VideoByTagList, \
    VideoCreate, LikeList, LikeView
from .views_web import TagList, VideoEdit, VideoDelete

urlpatterns = [
    # Include comments application
    url(
        r'^\/(?P<video>\d+)/comments',
        include('videos.comments.urls_web', namespace='comments')
    ),

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

    # List of tags
    url(
      r'\/tags$',
      TagList.as_view(),
      name='tags'
    ),

    # List of Videos by Tags
    url(
        r'^\/tags/(?P<tags>[' + constants.TAGS_ALLOWED_CHARACTERS + \
        ',]+)$',
        VideoByTagList.as_view(),
        name='videos_by_tags'
    ),

    # Create a specific video
    url(
        r'^\/new$',
        VideoCreate.as_view(),
        name='video_create'
    ),

    # Edit a specific video
    url(
        r'^\/(?P<pk>\d+)/edit$',
        VideoEdit.as_view(),
        name='video_edit'
    ),

    # Delete a specific video
    url(
        r'^\/(?P<pk>\d+)/delete$',
        VideoDelete.as_view(),
        name='video_delete'
    ),

    # LikeList
    url(
        r'^\/(?P<pk>\d+)/likes',
        LikeList.as_view(),
        name='video_likes'
    ),

    # Like View (to effectuate the Like)
    url(
        r'\/(?P<pk>\d+)/like',
        LikeView.as_view(),
        name='video_like'
    ),
]
