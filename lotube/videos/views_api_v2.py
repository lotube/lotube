from annoying.functions import get_object_or_None
from django.http.response import HttpResponseForbidden, Http404
from django.shortcuts import get_object_or_404
from rest_framework import mixins, status
from rest_framework.decorators import detail_route
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet

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


class LikeAPIView(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.ListModelMixin,
                  GenericViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get_serializer(self, *args, **kwargs):
        video = self.kwargs['video']
        video_obj = get_object_or_404(Video, id=video)
        serializer_class = self.get_serializer_class()
        kwargs['context'] = self.get_serializer_context()
        kwargs['context']['video'] = video_obj
        return serializer_class(*args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        try:
            like = self.get_object()
            if like.user == request.user:
                rating = get_object_or_None(Rating, likes_register=like.user)
                rating.undo_like()
                self.perform_destroy(like)
            else:
                return HttpResponseForbidden
        except Http404:
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)
