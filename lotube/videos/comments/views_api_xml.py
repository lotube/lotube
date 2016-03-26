from core.mixins import XMLFromJSONView
from .views_api_json import CommentListJSON, CommentDetailJSON


class CommentListXML(XMLFromJSONView, CommentListJSON):
    pass


class CommentDetailXML(XMLFromJSONView, CommentDetailJSON):
    pass
