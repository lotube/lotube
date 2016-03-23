from django.conf.urls import url

from .views import UserList

urlpatterns = [
    # List of users
    url(
        r'^.json$',
        UserList.as_view(),
        name='users_json'
    ),

    url(
        r'^.xml',
        UserList.as_view(),
        name='users_xml'
    ),

    # Retrieve a specific user

    #url(
    #    r'^/(?P<user>[a-zA-Z0-9]+)$',
    #
    #)
]