from django.http import Http404
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, View, CreateView, DeleteView, UpdateView

from config import constants
from videos.models import Video
from .models import Comment
from core.mixins import CustomLoginRequiredMixin


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
    paginate_by = constants.PAGINATE_BY

    def get_queryset(self):
        return self.video_object.comments.all()


class CommentDetailMixin(CommentMixin, DetailView):
    model = Comment

    def get_object(self, queryset=None):
        return get_object_or_404(self.model,
                                 video=self.kwargs['video'],
                                 id=self.kwargs['pk']
                                 )


class OwnerRequiredMixin(CustomLoginRequiredMixin):

    def dispatch(self, request, **kwargs):
        if not request.user.is_authenticated():
            raise Http404('Not logged in')
        comment = get_object_or_404(Comment, pk=kwargs['pk'])
        if request.user != comment.user:
            raise Http404('Not the video owner')
        return super(OwnerRequiredMixin, self).dispatch(request, **kwargs)


class CommentAddMixin(CustomLoginRequiredMixin, CreateView):
    model = Comment

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.video = Video.objects.get(id=self.kwargs['video'])
        return super(CommentAddMixin, self).form_valid(form)


class CommentEditMixin(OwnerRequiredMixin, UpdateView):
    model = Comment

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.video = Video.objects.get(id=self.kwargs['video'])
        return super(CommentEditMixin, self).form_valid(form)


class CommentDeleteMixin(DeleteView):
    model = Comment

