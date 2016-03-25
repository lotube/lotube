from config import constants
from core.mixins import JSONView
from .mixins import VideoListMixin, VideoDetailMixin, VideoUserListMixin


class VideoListJSON(JSONView, VideoListMixin):
    """
    List of Videos
    """

    def craft_response(self, context, **response_kwargs):
        items = [{
            'id': db_video.id,
            'source_id': db_video.id,
            'source': constants.PROJECT_NAME,
            'user': db_video.user.user.username,
            'title': db_video.filename,
            'description': db_video.description,
            'created_at': db_video.created,
            'modified_at': db_video.modified,
            'video_filename': db_video.filename,
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
            'id': db_video.user_id,
            'source_id': db_video.user_id,
            'source': constants.PROJECT_NAME,
            'user': db_video.user.user.username,
            'title': db_video.filename,
            'description': db_video.description,
            'created_at': db_video.created,
            'modified_at': db_video.modified,
            'video_filename': db_video.filename,
        }
        return response


class VideoUserListJSON(JSONView, VideoUserListMixin):
    """
    Video user list
    """

    def craft_response(self, context, **response_kwargs):
        items = [{
            'id': db_video.id,
            'source_id': db_video.id,
            'source': constants.PROJECT_NAME,
            'user': db_video.user.user.username,
            'title': db_video.filename,
            'description': db_video.description,
            'created_at': db_video.created,
            'modified_at': db_video.modified,
            'video_filename': db_video.filename,
        } for db_video in context['video_list']]
        response = {
            'page_info': {
                'total_results': len(items),
                'results_page': len(items),
            },
            'items': items
        }
        return response
