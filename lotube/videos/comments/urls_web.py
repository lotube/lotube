from django.conf.urls import url

from .views_web import CommentList, CommentDetail


urlpatterns = [
    # List of Comments
    url(
        r'^$',
        CommentList.as_view(),
        name='comments'
    ),

    # Retrieve a specific Comment by id
    url(
        r'^\/(?P<pk>\d+)$',
        CommentDetail.as_view(),
        name='comment'
    ),
]