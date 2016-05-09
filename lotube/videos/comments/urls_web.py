from django.conf.urls import url

from .views_web import CommentAdd, CommentEdit

urlpatterns = [
    # List of Comments
    #url(
    #    r'^$',
    #    CommentList.as_view(),
    #    name='comments'
    #),

    # Retrieve a specific Comment by id
    #url(
    #    r'^\/(?P<pk>\d+)$',
    #    CommentDetail.as_view(),
    #    name='comment'
    #),

    # Create new comment
    url(
        r'^\/new',
        CommentAdd.as_view(),
        name='comment_add'
    ),

    url(
        r'^\/(?P<pk>\d+)/edit$',
        CommentEdit.as_view(),
        name='comment_edit'
    ),
]
