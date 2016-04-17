from django.core.urlresolvers import reverse
from core.mixins import JSONView, JSONListView
from .mixins import CommentListMixin, CommentDetailMixin


def _get_item(db_comment, request):
    href_relative_uri = reverse('api:videos:comments:comment',
                                kwargs={'video': db_comment.video.id,
                                        'pk': db_comment.id,
                                        'format': '.json'})
    return {
        'type': 'comment',
        'video_id': db_comment.video.id,
        'id': db_comment.id,
        'href': request.build_absolute_uri(href_relative_uri),
        'user': db_comment.user.username,
        'content': db_comment.content if not db_comment.is_removed else '',
        'created_at': db_comment.created,
        'modified_at': db_comment.modified,
        'is_removed': db_comment.is_removed
    }


class CommentListJSON(JSONListView, CommentListMixin):
    """
    List of Comments
    """

    def __init__(self):
        self.type = 'comment_list'
        self.items = []

    def craft_response(self, context, **response_kwargs):
        self.items = [_get_item(db_video, self.request)
                      for db_video in context['comment_list']]
        return super(CommentListJSON, self)\
            .craft_response(context, **response_kwargs)


class CommentDetailJSON(JSONView, CommentDetailMixin):
    """
    Comment details
    """

    def craft_response(self, context, **response_kwargs):
        db_video = context['object']
        return _get_item(db_video, self.request)
