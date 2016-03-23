from django.conf.urls import url

from .views_web import UserList

urlpatterns = [
    # List of users
    url (
        r'^$',
        UserList.as_view(),
        name='users'
    ),

    # Retrieve a specific user

    #url(
    #    r'^/(?P<user>[a-zA-Z0-9]+)$',
    #
    #)
]

