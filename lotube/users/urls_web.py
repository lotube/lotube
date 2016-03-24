from django.conf.urls import url

from .views_web import UserList, UserDetail

urlpatterns = [
    # List of users
    url(
        r'^$',
        UserList.as_view(),
        name='users'
    ),

    # Retrieve a specific user
    url(
        r'^\/(?P<username>[\w\d]+)$',
        UserDetail.as_view(),
        name='user'
    ),
]
