from django.conf.urls import url

from .views import test

urlpatterns = [
    # List of users
    url (
        r'^$',
        test,
        name='users'
    ),

    # Retrieve a specific user

    #url(
    #    r'^/(?P<user>[a-zA-Z0-9]+)$',
    #
    #)
]