from .mixins import CommentListMixin, CommentDetailMixin


class CommentList(CommentListMixin):
    template_name = 'videos/comments/comment_list.html'


class CommentDetail(CommentDetailMixin):
    template_name = 'videos/comments/comment_detail.html'
