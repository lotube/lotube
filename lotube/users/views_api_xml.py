import dicttoxml
from django.http import HttpResponse

from .views_api_json import UserListJSON


class UserListXML(UserListJSON):

    def render_to_response(self, context, **response_kwargs):
        response = self.craft_response(context, **response_kwargs)
        return HttpResponse(
            dicttoxml.dicttoxml(response),
            content_type="text/xml"
        )
