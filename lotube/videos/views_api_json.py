from core.mixins import JSONView
from .mixins import VideoListMixin, VideoDetailMixin


class VideoListJSON(JSONView, VideoListMixin):
    """
    List of Videos
    """

    def craft_response(self, context, **response_kwargs):
        items = [{
            'id': db_video.video.user_id,
            'source_id': db_video.video.user_id,
            'source': 'lotube',
            'user': db_video.video.user,
            'title': db_video.video.filename,
            'description': db_video.video.description,
            'created_at': db_video.video.created,
            'modified_at': db_video.video.modified,
            'video_filename': db_video.video.filename,
        } for db_video in context['video_list']]
        response = {
            'page_info': {
                'total_results': len(items),
                'results_page': len(items),
            },
            'items': items
        }
        return response


class VideoDetailJSON(JSONView, VideoDetailMixin):
    """
    Video details
    """

    def craft_response(self, context, **response_kwargs):
        db_video = context['object']
        response = {
            'id': db_video.video.user_id,
            'source_id': db_video.video.user_id,
            'source': 'lotube',
            'user': db_video.video.user,
            'title': db_video.video.filename,
            'description': db_video.video.description,
            'created_at': db_video.video.created,
            'modified_at': db_video.video.modified,
            'video_filename': db_video.video.filename,
        }
        return response
