from annoying.fields import AutoOneToOneField
from django.db import models

from core.models import LowerCaseCharField
from core.validators import Common
from users.models import User
from . import constants


class AbstractTimeStamped(models.Model):
    """
    Auto-updated created and modified fields
    """
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class AbstractVideo(AbstractTimeStamped):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=300)
    description = models.CharField(max_length=10000, blank=True, default='')
    filename = models.CharField(max_length=255, unique=True)
    tags = models.ManyToManyField('videos.Tag', related_name='videos')

    def __str__(self):
        return self.title

    class Meta:
        abstract = True


class AbstractAnalytic(models.Model):
    video = AutoOneToOneField('videos.Video', primary_key=True,
                              related_name='analytic')
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return str(self.video)

    class Meta:
        abstract = True


class AbstractComment(AbstractTimeStamped):
    user = models.ForeignKey(User)
    video = models.ForeignKey('videos.Video')
    content = models.CharField(max_length=10000)
    is_removed = models.BooleanField(default=False)

    def __str__(self):
        return self.content if self.content < 50 else self.content[:50] + '...'

    class Meta:
        abstract = True


class AbstractTag(models.Model):
    name = LowerCaseCharField(max_length=30,
                              validators=[Common.contains(constants.TAGS_ALLOWED_CHARACTERS)])

    def __str__(self):
        return self.name

    class Meta:
        abstract = True
