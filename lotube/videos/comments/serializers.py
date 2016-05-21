from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField, \
    reverse

from core.api_utils import ContextUtils
from videos.comments.models import Comment


class CommentSerializer(ModelSerializer):
    href = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()

    def get_href(self, obj):
        return ContextUtils(self.context) \
            .build_absolute_uri(
            reverse('api_v2:video-comments-detail',
                    [obj.video.id, obj.id]))

    def get_user(self, obj):
        return ContextUtils(self.context) \
            .build_absolute_uri(reverse('api_v2:users-detail', [obj.user.id]))

    def create(self, validated_data):
        # logged in required
        user = ContextUtils(self.context).logged_in_user()

        # create comments
        comment = Comment(**validated_data)
        comment.user = user
        comment.video = self.context['video']
        comment.save()

        return comment

    def update(self, instance, validated_data):
        instance.content = validated_data.get('content', instance.content)
        instance.save()

        return instance

    class Meta:
        model = Comment
        fields = ('id', 'href', 'user', 'video', 'created', 'modified',
                  'content',)
        read_only_fields = ('id', 'href', 'user', 'video', 'user', 'created',
                            'modified')
