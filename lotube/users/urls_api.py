from django.conf.urls import url

from core.loading import APIViewLoader
from .views_api_json import UserListJSON
from .views_api_xml import UserListXML

urlpatterns = [
    # List of users
    url(
        r'^(?P<format>(\.\w{1,4}))$',
        APIViewLoader.as_view(json=UserListJSON, xml=UserListXML),
        name='users'
    ),

    #url(
    #    r'^.xml',
    #    UserList.as_view(),
    #    name='users_xml'
    #),

    # Retrieve a specific user

    #url(
    #    r'^/(?P<user>[a-zA-Z0-9]+)$',
    #
    #)
]