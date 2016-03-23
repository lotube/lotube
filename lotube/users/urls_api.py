from django.conf.urls import url
from .views import test

urlpatterns = [
    # List of users
    url(
        r'^.json$',
        test,
        name='users_json'
    ),

    url(
        r'^.xml',
        test,
        name='users_xml'
    ),

    # Retrieve a specific user

    #url(
    #    r'^/(?P<user>[a-zA-Z0-9]+)$',
    #
    #)
]