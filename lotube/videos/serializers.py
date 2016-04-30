from rest_framework_json_api import serializers

from videos.models import Video, Thumbnail, Tag


class ThumbnailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Thumbnail
        fields = ('url', 'width', 'height')


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ('name',)


class VideoSerializer(serializers.ModelSerializer):
    thumbnail = ThumbnailSerializer(read_only=True)
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Video
        fields = ('id', 'id_source', 'source', 'title', 'description',
                  'duration', 'created', 'modified', 'filename', 'thumbnail',
                  'tags')
