from core.mixins import XMLFromJSONView
from .views_api_json import VideoListJSON, VideoDetailJSON, VideoUserListJSON, \
    VideoAnalyticJSON, VideoRatingJSON, TagListJSON


class VideoListXML(XMLFromJSONView, VideoListJSON):
    pass


class VideoDetailXML(XMLFromJSONView, VideoDetailJSON):
    pass


class VideoUserListXML(XMLFromJSONView, VideoUserListJSON):
    pass


class VideoAnalyticXML(XMLFromJSONView, VideoAnalyticJSON):
    pass


class VideoRatingXML(XMLFromJSONView, VideoRatingJSON):
    pass


class VideoByTagListXML(XMLFromJSONView, VideoAnalyticJSON):
    pass


class TagListXML(XMLFromJSONView, TagListJSON):
    pass
