from rest_framework import serializers
from rest_framework.serializers import SerializerMethodField, reverse, \
    HyperlinkedIdentityField
from rest_framework.serializers import ModelSerializer

from core.api_utils import ContextUtils
from videos.models import Video, Thumbnail, Tag, Analytic, Rating
from videos.utils import TagBuilder


class RatingSerializer(ModelSerializer):

    class Meta:
        model = Rating
        fields = ('upvotes', 'downvotes')


class AnalyticsSerializer(ModelSerializer):

    class Meta:
        model = Analytic
        fields = ('views', 'unique_views', 'shares')


class ThumbnailSerializer(ModelSerializer):

    class Meta:
        model = Thumbnail
        fields = ('url', 'width', 'height')
        read_only_fields = ('width', 'height')


class TagSerializer(ModelSerializer):

    class Meta:
        model = Tag
        fields = ('name',)


class VideoSerializer(ModelSerializer):
    href = HyperlinkedIdentityField(view_name='api_v2:videos-detail')
    thumbnail = ThumbnailSerializer()
    tags = TagSerializer(many=True, read_only=True)
    user = serializers.SerializerMethodField()
    analytics = SerializerMethodField()
    comments = serializers.SerializerMethodField()

    def get_analytics(self, obj):
        return ContextUtils(self.context)\
            .build_absolute_uri(reverse('api_v2:videos-analytics', [obj.id]))

    def get_user(self, obj):
        return ContextUtils(self.context)\
            .build_absolute_uri(reverse('api_v2:users-detail', [obj.user.id]))

    def get_comments(self, obj):
        return ContextUtils(self.context)\
            .build_absolute_uri(reverse('api_v2:video-comments-list', [obj.id]))

    def create(self, validated_data):
        thumbnail = validated_data.pop('thumbnail')

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

        # add video thumbnail
        video.thumbnail.url = thumbnail['url']

        return video

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.filename = validated_data.get('filename', instance.filename)

        # thumbnail
        thumbnail = validated_data.get('thumbnail', instance.thumbnail).popitem()
        instance.thumbnail.url = thumbnail[1] if thumbnail[0] == 'url' else ''

        return instance

    class Meta:
        model = Video
        fields = ('id', 'id_source', 'source', 'user', 'href', 'title',
                  'description', 'duration', 'created', 'modified', 'filename',
                  'thumbnail', 'analytics', 'tags', 'comments',)
        read_only_fields = ('id_source', 'source', 'user', 'href', 'duration',
                            'comments',)
