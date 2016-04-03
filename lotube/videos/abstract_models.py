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
    id_source = models.CharField(max_length=100, unique=True)
    source = models.CharField(max_length=30)
    user = models.ForeignKey(User)
    title = models.CharField(max_length=300)
    description = models.CharField(max_length=10000, blank=True, default='')
    duration = models.PositiveIntegerField(default=0)
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
    unique_views = models.PositiveIntegerField(default=0)
    shares = models.PositiveIntegerField(default=0)

    def __str__(self):
        return str(self.video)

    class Meta:
        abstract = True


class AbstractRating(models.Model):
    video = AutoOneToOneField('videos.Analytic', primary_key=True,
                              related_name='rating')
    upvotes = models.PositiveIntegerField(default=0)
    downvotes = models.PositiveIntegerField(default=0)


class AbstractThumbnail(models.Model):
    video = AutoOneToOneField('videos.Video', primary_key=True,
                              related_name='thumbnail')
    url = models.CharField(max_length=255, unique=True)
    width = models.PositiveIntegerField(default=0)
    height = models.PositiveIntegerField(default=0)


class AbstractTag(models.Model):
    name = LowerCaseCharField(max_length=30,
                              unique=True,
                              validators=[Common.contains(constants.TAGS_ALLOWED_CHARACTERS)])

    def __str__(self):
        return self.name

    class Meta:
        abstract = True
