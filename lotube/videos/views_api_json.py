from django.core.urlresolvers import reverse
from django.http import Http404

from core.mixins import JSONView
from .mixins import VideoListMixin, VideoDetailMixin, VideoUserListMixin
from .mixins import VideoByTagListMixin, TagListMixin


def _get_item(db_video, request):
    href_relative_uri = reverse('api:videos:video',
                                kwargs={'pk': db_video.id,
                                        'format': '.json'})
    return {
        'type': 'video',
        'id': {
            'id': db_video.id,
            'id_source': db_video.id_source,
        },
        'href': request.build_absolute_uri(href_relative_uri),
        'source': db_video.source,
        'user': db_video.user.username,
        'title': db_video.title,
        'description': db_video.description,
        'duration': db_video.duration,
        'created_at': db_video.created,
        'modified_at': db_video.modified,
        'filename': db_video.filename,
        'thumbnail': {
            'height': db_video.thumbnail.height,
            'width': db_video.thumbnail.width,
            'url': db_video.thumbnail.url
        },
        'tags': [tag.name for tag in db_video.tags.all()]
    }


class VideoListJSON(JSONView, VideoListMixin):
    """
    List of Videos
    """

    def craft_response(self, context, **response_kwargs):
        items = [_get_item(db_video, self.request)
                 for db_video in context['video_list']]

        def url_params(request, context, overwrite_param={}):
            """
            :param request: page (list) request with or without page param
            :param context: page context
            :param overwrite_param: dict of params to overwrite (i.e) {'page':1}
            If the parameter doesn't exist in the original request, it will
            be appended.
            :return: url params (textual) (i.e. ?page=2)
            """

            params = [(param, str(request.GET[param]
                                  if param not in overwrite_param
                                  else overwrite_param.pop(param)))
                      for param in request.GET]
            for key, value in overwrite_param.iteritems():  # not in the original request
                params.append((key, str(value)))

            params_str = map(lambda param: param[0] + '=' + param[1], params)
            params_str = '?' + '&'.join(params_str) if url_params else ''
            return params_str

        def gen_page_link(request, context, page):
            relative_uri = reverse('api:videos:videos', kwargs=self.kwargs)
            params = url_params(request, context, {'page': page})

            return request.build_absolute_uri(relative_uri + params) \
                if params != '' else ''

        page_obj = context['page_obj']
        link_self = gen_page_link(self.request, context, page_obj.number)
        link_first = gen_page_link(self.request, context, 1)
        link_prev = gen_page_link(self.request, context,
                                  page_obj.previous_page_number()) \
            if page_obj.has_previous() else ''
        link_next = gen_page_link(self.request, context,
                                  page_obj.next_page_number()) \
            if page_obj.has_next() else ''
        link_last = gen_page_link(self.request, context,
                                  page_obj.paginator.num_pages)

        response = {
            'type': 'video_list',
            'page_info': {
                'total_results': len(items),
                'results_page': len(items),
                'page': 1,
            },
            'links': {
                'self': link_self,
                'first': link_first,
                'previous': link_prev,
                'next': link_next,
                'last': link_last,
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
        return _get_item(db_video, self.request)


class VideoUserListJSON(JSONView, VideoUserListMixin):
    """
    Video user list
    """

    def craft_response(self, context, **response_kwargs):
        items = [_get_item(db_video, self.request)
                 for db_video in context['video_list']]
        response = {
            'type': 'video_list',
            'page_info': {
                'total_results': len(items),
                'results_page': len(items),
                'page': 1
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
        href_relative_uri = reverse('api:videos:video_analytic',
                                    kwargs={'pk': db_video.id,
                                            'format': '.json'})
        response = {
            'type': 'video_analytic',
            'href': self.request.build_absolute_uri(href_relative_uri),
            'video_id': db_video.id,
            'views': {
                'total_views': db_video.analytic.views,
                'unique_views': db_video.analytic.unique_views,
            },
            'shares': db_video.analytic.shares,
        }
        return response


class VideoRatingJSON(JSONView, VideoDetailMixin):
    """
    Video rating
    """

    def craft_response(self, context, **response_kwargs):
        db_video = context['object']
        href_relative_uri = reverse('api:videos:video_rating',
                                    kwargs={'pk': db_video.id,
                                            'format': '.json'})
        response = {
            'type': 'video_rating',
            'href': self.request.build_absolute_uri(href_relative_uri),
            'video_id': db_video.id,
            'upvotes': db_video.rating.upvotes,
            'downvotes': db_video.rating.downvotes,
        }
        return response


class VideoByTagListJSON(JSONView, VideoByTagListMixin):
    """
    List of videos by Tags
    """

    def craft_response(self, context, **response_kwargs):
        items = [_get_item(db_video, self.request)
                 for db_video in context['video_list']]
        response = {
            'type': 'video_list',
            'page_info': {
                'total_results': len(items),
                'results_page': len(items),
                'page': 1
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
        response = {
            'type': 'tag_list',
            'page_info': {
                'total_results': len(tags),
                'results_page': len(tags),
                'page': 1
            },
            'tags': tags
        }
        return response
