from django.http import HttpResponse

from core.mixins import XMLFromJSONView
from .views_api_json import VideoListJSON, VideoDetailJSON


class VideoListXML(XMLFromJSONView, VideoListJSON):
    pass


class VideoDetailXML(XMLFromJSONView, VideoDetailJSON):
    pass
