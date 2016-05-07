from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField, \
    reverse

from core.api_utils import ContextUtils
from videos.comments.models import Comment


class CommentHrefHyperlinkedIdentityField(HyperlinkedIdentityField):
    video = None

    def __init__(self, **kwargs):
        super(CommentHrefHyperlinkedIdentityField, self).__init__(**kwargs)

    def get_url(self, obj, view_name, request, format):
        lookup_field_value = getattr(obj, self.lookup_field, None)

        return ContextUtils(self.context) \
            .build_absolute_uri(
            reverse('api_v2:video-comments-detail',
                    [self.video.id, lookup_field_value]))


class CommentSerializer(ModelSerializer):
    href = CommentHrefHyperlinkedIdentityField(view_name='api_v2:video-comments-detail')

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

        return instance

    class Meta:
        model = Comment
        fields = ('id', 'href', 'video', 'user', 'created', 'modified',
                  'content',)
        read_only_fields = ('id', 'href', 'video', 'user', 'created',
                            'modified')
