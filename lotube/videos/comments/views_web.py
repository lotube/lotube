from django.core.urlresolvers import reverse

from .mixins import CommentListMixin, CommentDetailMixin, CommentAddMixin, CommentEditMixin, CommentDeleteMixin
from .forms import CommentAddForm, CommentEditForm

#class CommentList(CommentListMixin):
#    template_name = 'videos/comments/comment_list.html'


#class CommentDetail(CommentDetailMixin):
#    template_name = 'videos/comments/comment_detail.html'


class CommentAdd(CommentAddMixin):
    template_name = 'videos/comments/comment_add.html'
    form_class = CommentAddForm

    def get_success_url(self):
        return reverse('web:videos:video', args=(self.kwargs['video']))


class CommentEdit(CommentEditMixin):
    template_name = 'videos/comments/comment_edit.html'
    form_class = CommentEditForm

    def get_success_url(self):
        return reverse('web:videos:video', args=(self.kwargs['video']))
