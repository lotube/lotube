from django.http import JsonResponse, HttpResponse
from django.views.generic import View


class JSONView(View):
    """
    Defines what a JSON View should have at least.
    It very recommended to use along with a generic view (ListView,
    DetailView...), since it works overriding the render_to_response method.
    """

    def craft_response(self, context, **response_kwargs):
        """
        Should return a dictionary of data to be returned to the user.
        """
        return {}

    def render_to_response(self, context, **response_kwargs):
        response = self.craft_response(context, **response_kwargs)
        return JsonResponse(response)


class XMLView(View):

    def craft_response(self, context, **response_kwargs):
        """
        Should return an XML structure to be returned to the user.
        """
        return '<root></root>'

    def render_to_response(self, context, **response_kwargs):
        response = self.craft_response(context, **response_kwargs)
        return HttpResponse(
            response,
            content_type="text/xml"
        )
