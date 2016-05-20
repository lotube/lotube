from django.shortcuts import get_object_or_404
from rest_framework.decorators import detail_route
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from core.api_utils import IsOwnerOrReadOnly
from videos.models import Video, Tag, Analytic, Rating, Like
from videos.serializers import VideoSerializer, TagSerializer, \
    AnalyticsSerializer, RatingSerializer, LikeSerializer


class VideoAPIView(ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    @detail_route(url_path='analytics')
    def get_analytics(self, request, pk):
        obj = get_object_or_404(Analytic, pk=pk)
        serializer = AnalyticsSerializer(obj)
        return Response(serializer.data)

    @detail_route(url_path='rating')
    def get_rating(self, request, pk):
        obj = get_object_or_404(Rating, pk=pk)
        kwargs = {'request': request}
        serializer = RatingSerializer(obj, **kwargs)
        return Response(serializer.data)


class TagAPIView(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class LikeAPIView(ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get_serializer_context(self):
        return {'request': self.request}
