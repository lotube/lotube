from django.db import models


class TagManager(models.Manager):

    def get_videos_by_tags(self, tags):
        """
        Returns a Video queryset containing the videos which match at least one
        of the tags.
        Tags: coma-separated string list of tags, no space between tags is
            needed.
        """
        queryset = self.none()
        tags = map(lambda x: x.strip(), tags.split(','))
        for tag in tags:
            queryset = queryset | self.filter(name=tag)
        return queryset
