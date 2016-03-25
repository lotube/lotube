from django.conf.urls import url

from core.loading import APIViewLoader
from .views_api_json import VideoListJSON, VideoDetailJSON
from .views_api_xml import VideoListXML, VideoDetailXML


data_format = '(?P<format>\.\w{1,4})'
urlpatterns = [
    #List of Videos
    url(
        r'^' + data_format + '$',
        APIViewLoader.as_view(json=VideoListJSON, xml=VideoListXML),
        name='videos'
    ),

    #Retrieve a specific Video
    url(
        r'^\/(?P<pk>\d+)' + data_format + '$',
        APIViewLoader.as_view(json=VideoDetailJSON, xml=VideoDetailXML),
        name='video'
    ),
]
