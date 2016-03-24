from django.conf.urls import url

from core.loading import APIViewLoader
from .views_api_json import UserListJSON, UserDetailJSON
from .views_api_xml import UserListXML, UserDetailXML


data_format = '(?P<format>(\.\w{1,4}))'
urlpatterns = [
    # List of users
    url(
        r'^' + data_format + '$',
        APIViewLoader.as_view(json=UserListJSON, xml=UserListXML),
        name='users'
    ),

    # Retrieve a specific user
    url(
        r'^\/(?P<username>[\w\d]+)' + data_format + '$',
        APIViewLoader.as_view(json=UserDetailJSON, xml=UserDetailXML),
        name='user'
    ),
]
