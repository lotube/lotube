from config import constants
from core.mixins import JSONView
from .mixins import VideoListMixin, VideoDetailMixin, VideoUserListMixin
from .mixins import VideoByTagListMixin, TagListMixin


def _get_item(db_video):
    return {
        'id': db_video.id,
        'source_id': db_video.id,
        'source': constants.PROJECT_NAME,
        'user': db_video.user.username,
        'title': db_video.title,
        'description': db_video.description,
        'created_at': db_video.created,
        'modified_at': db_video.modified,
        'video_filename': db_video.filename,
        'tags': [tag.name for tag in db_video.tags.all()]
    }


class VideoListJSON(JSONView, VideoListMixin):
    """
    List of Videos
    """

    def craft_response(self, context, **response_kwargs):
        items = [_get_item(db_video) for db_video in context['video_list']]
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
        return _get_item(db_video)


class VideoUserListJSON(JSONView, VideoUserListMixin):
    """
    Video user list
    """

    def craft_response(self, context, **response_kwargs):
        items = [_get_item(db_video) for db_video in context['video_list']]
        response = {
            'page_info': {
                'total_results': len(items),
                'results_page': len(items),
            },
            'items': items
        }
        return response


class VideoAnalyticJSON(JSONView, VideoDetailMixin):
    """
    Video analytic
    """

    def craft_response(self, context, **response_kwargs):
        db_video = context['object']
        response = {
            'id': db_video.id,
            'views': db_video.analytic.views,
        }
        return response


class VideoByTagListJSON(JSONView, VideoByTagListMixin):
    """
    List of videos by Tags
    """

    def craft_response(self, context, **response_kwargs):
        items = [_get_item(db_video) for db_video in context['video_list']]
        response = {
            'page_info': {
                'total_results': len(items),
                'results_page': len(items),
            },
            'items': items
        }
        return response


class TagListJSON(JSONView, TagListMixin):
    """
    List of all tags
    """

    def craft_response(self, context, **response_kwargs):
        tags = [tag.name for tag in context['tag_list']]
        print tags
        response = {
            'page_info': {
                'total_results': len(tags),
                'results_page': len(tags),
            },
            'tags': tags
        }
        return response
