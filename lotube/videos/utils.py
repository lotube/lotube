from django.core.exceptions import ValidationError

from videos.models import Tag
from .constants import MIN_TAGS, MAX_TAGS


class TagBuilder(object):
    """
    Creates or Gets existing DB tags.
    """

    @staticmethod
    def get_or_create_tag(tag_name):
        """
        Returns a Tag, which will be either created or retrieved from the
        database.
        """
        tag_name = tag_name.strip()
        if tag_name == '':
            raise ValueError('Tag value cannot be empty')

        try:
            return Tag.objects.get(name=tag_name)
        except Tag.DoesNotExist:
            tag = Tag(name=tag_name)
            tag.save()
            return tag

    @staticmethod
    def get_or_create_tags(text):
        """
        Returns a list of Tag from the provided text, which will be either
        created or retrieved from the database.
        """
        text = text.strip()
        if text == '':
            raise ValueError('Tag value cannot be empty')

        return [TagBuilder.get_or_create_tag(tag)
                for tag in TagBuilder._get_tags_str(text)]

    @staticmethod
    def _get_tags_str(title):
        """
        Gets tags str from title.
        """
        tags = filter(lambda x: len(x) > 2, title.split())
        if not tags:
            return title.split()[:MIN_TAGS]  # Minimum of tags
        return tags[:MAX_TAGS]
