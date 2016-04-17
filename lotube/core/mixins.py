import dicttoxml
from django.core.urlresolvers import reverse
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


class JSONListView(JSONView):
    """
    JSON common ListView with type, pagination and items.
    """

    def __init__(self, **kwargs):
        super(JSONListView, self).__init__(**kwargs)
        self.type = 'list'
        self.items = []

    def page_info(self, context):
        page_obj = context['page_obj']
        return {
                'total_results': page_obj.paginator.count,
                'results_page': len(page_obj),
                'page': page_obj.number,
        }

    def links(self, context):
        page_obj = context['page_obj']
        link_self = self.__gen_page_link(self.request, page_obj.number)
        link_first = self.__gen_page_link(self.request, 1)
        link_previous = self.__gen_page_link(self.request,
                                             page_obj.previous_page_number()) \
            if page_obj.has_previous() else ''
        link_next = self.__gen_page_link(self.request,
                                         page_obj.next_page_number()) \
            if page_obj.has_next() else ''
        link_last = self.__gen_page_link(self.request,
                                         page_obj.paginator.num_pages)
        return {
            'self': link_self,
            'first': link_first,
            'previous': link_previous,
            'next': link_next,
            'last': link_last,
        }

    def craft_response(self, context, **response_kwargs):
        response = {
            'type': self.type,
            'page_info': self.page_info(context),
            'links': self.links(context),
            'items': self.items
        }
        return response

    def __url_params(self, request, overwrite_param={}):
            """
            :param request: page (list) request with or without page param
            :param context: page context
            :param overwrite_param: dict of params to overwrite (i.e) {'page':1}
            If the parameter doesn't exist in the original request, it will
            be appended.
            :return: url params (textual) (i.e. ?page=2)
            """

            params = [(param, str(request.GET[param]
                                  if param not in overwrite_param
                                  else overwrite_param.pop(param)))
                      for param in request.GET]
            for key, value in overwrite_param.iteritems():  # not in the original request
                params.append((key, str(value)))

            params_str = map(lambda param: param[0] + '=' + param[1], params)
            params_str = '?' + '&'.join(params_str) if params else ''
            return params_str

    def __gen_page_link(self, request, page):
            relative_uri = reverse('api:videos:videos', kwargs=self.kwargs)
            params = self.__url_params(request, {'page': page})

            return request.build_absolute_uri(relative_uri + params) \
                if params != '' else ''


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


class XMLFromJSONView(View):

    def render_to_response(self, context, **response_kwargs):
        response = self.craft_response(context, **response_kwargs)
        return HttpResponse(
            dicttoxml.dicttoxml(response),
            content_type="text/xml"
        )
