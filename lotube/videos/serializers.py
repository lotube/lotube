from rest_framework import serializers
from rest_framework.serializers import SerializerMethodField, reverse, \
    HyperlinkedIdentityField
from rest_framework.serializers import ModelSerializer

from core.api_utils import ContextUtils
from videos.models import Video, Tag, Analytic, Rating, Like
from videos.utils import TagBuilder


class LikeSerializer(ModelSerializer):
    href = SerializerMethodField()
    video = SerializerMethodField()

    def get_href(self, obj):
        return ContextUtils(self.context)\
            .build_absolute_uri(reverse('api_v2:video-likes-detail',
                                        [obj.rating.video.id, obj.id]))

    def get_video(self, obj):
        return obj.rating.video.id

    class Meta:
        model = Like
        fields = ('href', 'video', 'rating', 'user', 'created', 'modified',)


class RatingSerializer(ModelSerializer):
    href = HyperlinkedIdentityField(view_name='api_v2:videos-rating')
    likes_count = serializers.SerializerMethodField()
    likes = serializers.SerializerMethodField()

    def __init__(self, obj, *args, **kwargs):
        request = kwargs.pop('request')
        super(RatingSerializer, self).__init__(obj, *args, **kwargs)
        self.context['request'] = request

    def get_likes_count(self, obj):
        return obj.likes

    def get_likes(self, obj):
        return ContextUtils(self.context)\
            .build_absolute_uri(reverse('api_v2:video-likes-list', [obj.video.id]))

    class Meta:
        model = Rating
        fields = ('video', 'href', 'likes_count', 'likes',)


class AnalyticsSerializer(ModelSerializer):

    class Meta:
        model = Analytic
        # fields = ('views', 'unique_views', 'shares')
        fields = ('views',)


class TagSerializer(ModelSerializer):

    class Meta:
        model = Tag
        fields = ('name',)


class VideoSerializer(ModelSerializer):
    href = HyperlinkedIdentityField(view_name='api_v2:videos-detail')
    tags = TagSerializer(many=True, read_only=True)
    user = serializers.SerializerMethodField()
    analytics = SerializerMethodField()
    rating = SerializerMethodField()
    comments = serializers.SerializerMethodField()

    def get_analytics(self, obj):
        return ContextUtils(self.context)\
            .build_absolute_uri(reverse('api_v2:videos-analytics', [obj.id]))

    def get_user(self, obj):
        return ContextUtils(self.context)\
            .build_absolute_uri(reverse('api_v2:users-detail', [obj.user.id]))

    def get_rating(self, obj):
        return ContextUtils(self.context)\
            .build_absolute_uri(reverse('api_v2:videos-rating', [obj.id]))

    def get_comments(self, obj):
        return ContextUtils(self.context)\
            .build_absolute_uri(reverse('api_v2:video-comments-list', [obj.id]))

    def create(self, validated_data):
        # logged in required
        user = ContextUtils(self.context).logged_in_user()

        # create video
        video = Video(**validated_data)
        video.user = user
        video.save()

        # add video tags
        tags = TagBuilder.get_or_create_tags(validated_data['title'])
        for tag in tags:
            video.tags.add(tag)

        return video

    class Meta:
        model = Video
        fields = ('id', 'id_source', 'source', 'user', 'href', 'title',
                  'description', 'duration', 'created', 'modified', 'filename',
                  'thumbnail', 'analytics', 'rating', 'tags', 'comments',)
        read_only_fields = ('id_source', 'source', 'user', 'href', 'duration',
                            'comments',)
