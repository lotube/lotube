from config import constants
from core.mixins import JSONView
from .mixins import CommentListMixin, CommentDetailMixin


def _get_item(db_comment):
    return {
        'type': 'comment',
        'video_id': db_comment.video.id,
        'id': db_comment.id,
        'user': db_comment.user.username,
        'content': db_comment.content if not db_comment.is_removed else '',
        'created_at': db_comment.created,
        'modified_at': db_comment.modified,
        'is_removed': db_comment.is_removed
    }


class CommentListJSON(JSONView, CommentListMixin):
    """
    List of Comments
    """

    def craft_response(self, context, **response_kwargs):
        items = [_get_item(db_video) for db_video in context['comment_list']]
        response = {
            'page_info': {
                'total_results': len(items),
                'results_page': len(items),
                'page': 1,
            },
            'items': items
        }
        return response


class CommentDetailJSON(JSONView, CommentDetailMixin):
    """
    Comment details
    """

    def craft_response(self, context, **response_kwargs):
        db_video = context['object']
        return _get_item(db_video)
