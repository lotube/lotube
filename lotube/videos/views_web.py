from annoying.functions import get_object_or_None
from django.core.urlresolvers import reverse
from django.db import transaction
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.views.generic import ListView
from django.views.generic.base import RedirectView

from .models import Like, Video
from .mixins import VideoListMixin, VideoDetailMixin, VideoUserListMixin, \
    VideoCreateMixin
from .mixins import VideoByTagListMixin, TagListMixin, VideoEditMixin, \
    VideoDeleteMixin
from .forms import VideoEditForm, VideoCreateForm


class VideoList(VideoListMixin):
    template_name = 'videos/video_list.html'


class VideoDetail(VideoDetailMixin):
    template_name = 'videos/video_detail.html'


class VideoUserList(VideoUserListMixin):
    template_name = 'videos/video_list.html'


class VideoByTagList(VideoByTagListMixin):
    template_name = 'videos/video_list.html'


class TagList(TagListMixin):
    template_name = 'videos/tag_list.html'


class VideoCreate(VideoCreateMixin):
    template_name = 'videos/video_create.html'
    form_class = VideoCreateForm

    def get_success_url(self):
        return reverse('web:videos:video', args=[self.object.id])


class VideoEdit(VideoEditMixin):
    template_name = 'videos/video_edit.html'
    form_class = VideoEditForm

    def get_success_url(self):
        return reverse('web:videos:video_edit', args=[self.kwargs['pk']])


class VideoDelete(VideoDeleteMixin):
    template_name = 'videos/video_delete.html'
    success_url = '/'


class LikeList(ListView):
    template_name = 'videos/like_list.html'
    model = Like

    def get_context_data(self, **kwargs):
        context = super(LikeList, self).get_context_data()
        context['video'] = self.kwargs['pk']
        return context


class LikeView(RedirectView):
    pattern_name = 'web:videos:video'

    @method_decorator(csrf_protect)
    @transaction.atomic
    def post(self, request, *args, **kwargs):
        video_obj = get_object_or_404(Video, id=self.kwargs['pk'])
        rating_obj = video_obj.rating
        like_obj = get_object_or_None(Like, rating=rating_obj,
                                      user=request.user)
        if like_obj is None:
            rating_obj.like()
            like_obj = Like(rating=rating_obj,
                            user=request.user)
            like_obj.save()

        return super(LikeView, self).post(request, *args, **kwargs)
