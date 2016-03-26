from django.conf.urls import url

from core.loading import APIViewLoader
from .views_api_json import CommentListJSON, CommentDetailJSON
from .views_api_xml import CommentListXML, CommentDetailXML

data_format = '(?P<format>\.\w{1,4})'
urlpatterns = [
    # List of Comments
    url(
        r'^' + data_format + '$',
        APIViewLoader.as_view(json=CommentListJSON, xml=CommentListXML),
        name='comments'
    ),

    # Retrieve a specific Comment by id
    url(
        r'^\/(?P<pk>\d+)' + data_format + '$',
        APIViewLoader.as_view(json=CommentDetailJSON, xml=CommentDetailXML),
        name='comment'
    ),
]
