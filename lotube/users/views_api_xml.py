from core.mixins import XMLFromJSONView
from .views_api_json import UserListJSON, UserDetailJSON


class UserListXML(XMLFromJSONView, UserListJSON):
    pass


class UserDetailXML(XMLFromJSONView, UserDetailJSON):
    pass
