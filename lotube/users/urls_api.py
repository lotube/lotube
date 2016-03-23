from django.conf.urls import url

from .views_api import UserListJSON

urlpatterns = [
    # List of users
    url(
        r'^.json$',
        UserListJSON.as_view(),
        name='users_json'
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