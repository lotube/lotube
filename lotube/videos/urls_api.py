from django.conf.urls import include, url

from core.loading import APIViewLoader
from . import constants
from .views_api_json import VideoListJSON, VideoDetailJSON, VideoUserListJSON
from .views_api_json import VideoAnalyticJSON, VideoByTagListJSON, TagListJSON
from .views_api_xml import VideoListXML, VideoDetailXML, VideoUserListXML
from .views_api_xml import VideoAnalyticXML, VideoByTagListXML, TagListXML


data_format = '(?P<format>\.\w{1,4})'
urlpatterns = [
    # Include comments application
    url(
        r'^\/(?P<video>\d+)/comments',
        include('videos.comments.urls_api', namespace='comments')
    ),

    # List of Videos
    url(
        r'^' + data_format + '$',
        APIViewLoader.as_view(json=VideoListJSON, xml=VideoListXML),
        name='videos'
    ),

    # Retrieve a specific Video
    url(
        r'^\/(?P<pk>\d+)' + data_format + '$',
        APIViewLoader.as_view(json=VideoDetailJSON, xml=VideoDetailXML),
        name='video'
    ),

    # List of Videos by User
    url(
        r'^\/user/(?P<username>[\w\d]+)' + data_format + '$',
        APIViewLoader.as_view(json=VideoUserListJSON, xml=VideoUserListXML),
        name='user_videos'
    ),

    # Video analytic
    url(
        r'^\/(?P<pk>\d+)/analytics' + data_format + '$',
        APIViewLoader.as_view(json=VideoAnalyticJSON, xml=VideoAnalyticXML),
        name='video_analytic'
    ),

    # List of all tags
    url(
        r'^\/tags' + data_format + '$',
        APIViewLoader.as_view(json=TagListJSON, xml=TagListXML),
        name='tag_list'
    ),

    # List of Videos by Tags
    url(
        r'^\/tags/(?P<tags>[' + constants.TAGS_ALLOWED_CHARACTERS + \
        ',]+)' + data_format + '$',
        APIViewLoader.as_view(json=VideoByTagListJSON, xml=VideoByTagListXML),
        name='videos_by_tags'
    ),
]
