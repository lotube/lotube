from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, View

from videos.models import Video
from .models import Comment


class CommentMixin(View):
    """
    Basic mixin that shall be imported by every comment.

    It does check whether the video provided in the URL is valid. Otherwise,
    it throws a 404.

    You can use:
    self.video_object = database object of the requested video
    """

    def dispatch(self, request, *args, **kwargs):
        self.video_object = get_object_or_404(Video, id=kwargs['video'])
        return super(CommentMixin, self).dispatch(request, args, kwargs)


class CommentListMixin(CommentMixin, ListView):
    model = Comment

    def get_queryset(self):
        return self.video_object.comments.all()


class CommentDetailMixin(CommentMixin, DetailView):
    model = Comment

    def get_object(self, queryset=None):
        return get_object_or_404(self.model,
                                 video=self.kwargs['video'],
                                 id=self.kwargs['pk']
                                 )

