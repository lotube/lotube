from core.mixins import XMLFromJSONView
from .views_api_json import VideoListJSON, VideoDetailJSON, VideoUserListJSON
from .views_api_json import VideoAnalyticJSON


class VideoListXML(XMLFromJSONView, VideoListJSON):
    pass


class VideoDetailXML(XMLFromJSONView, VideoDetailJSON):
    pass


class VideoUserListXML(XMLFromJSONView, VideoUserListJSON):
    pass


class VideoAnalyticXML(XMLFromJSONView, VideoAnalyticJSON):
    pass
