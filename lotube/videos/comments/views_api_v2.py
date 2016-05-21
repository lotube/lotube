from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from core.api_utils import IsOwnerOrReadOnly
from videos.comments.serializers import CommentSerializer
from videos.models import Video
from .models import Comment


class CommentAPIView(ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def _get_video(self):
        return get_object_or_404(Video, id=self.kwargs['video'])

    def get_queryset(self):
        return Comment.objects.filter(video=self._get_video(), is_removed=False)

    def get_serializer_context(self):
        return {'request': self.request, 'video': self._get_video()}
