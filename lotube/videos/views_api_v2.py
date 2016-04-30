from rest_framework import viewsets

from videos.models import Video
from videos.serializers import VideoSerializer, ThumbnailSerializer


class VideosListView(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
