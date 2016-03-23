from django.http import Http404


class APIViewLoader:
    """
    Utility for resolving various url api formats within the same URL, which
    works the very same way as the Class Based Views in Django.

    Accepted formats have to be sent through the format request parameter, like:
    r'^api/users(?P<format>(\.json|\.xml)

    View loader will then be:
    APIViewLoader.as_view(json=MyJSONView, xml=MyXMLView)

    Example url:
    url(
        r'^(?P<format>(\.json|\.xml))$',
        APIViewLoader.as_view(json=UserListJSON, xml=UserListXML),
        name='users'
    )
    """

    def __init__(self, formats):
        """
        :param formats: {format: <class>} (i.e. json: 'ListUsersJSON')
        :return:
        """
        self.formats = formats

    def request_handler(self, request, *args, **kwargs):
        request_format = self.clean_format(kwargs['format'])
        if not request_format in self.formats:
            raise Http404("{0} format is not available".format(request_format))
        return self.formats[request_format].as_view()(request, *args, **kwargs)

    def clean_format(self, format):
        """
        :param format: a .format or format
        :return: a format name (with no dot at the start)
        """
        return format[1:] if format[0] == '.' else format

    @classmethod
    def as_view(cls, **kwargs):
        return cls(kwargs).request_handler
