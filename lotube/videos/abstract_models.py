from django.db import models
from django.db.models import OneToOneField

from core.models import LowerCaseCharField
from core.validators import Common
from users.models import User
from .managers import TagManager
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
    # Video is from LoTube if source and id_source are empty
    id_source = models.CharField(max_length=100, blank=True)
    source = models.CharField(max_length=30, blank=True)
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
    video = OneToOneField('videos.Video', primary_key=True,
                          related_name='analytic')
    views = models.PositiveIntegerField(default=0)
    unique_views = models.PositiveIntegerField(default=0)
    shares = models.PositiveIntegerField(default=0)

    def __str__(self):
        return str(self.video)

    class Meta:
        abstract = True


class AbstractRating(models.Model):
    video = OneToOneField('videos.Video', primary_key=True,
                          related_name='rating')
    upvotes = models.PositiveIntegerField(default=0)
    downvotes = models.PositiveIntegerField(default=0)

    @property
    def upvote(self):
        self.upvotes += 1
        self.save()
        return self.upvotes

    @property
    def downvote(self):
        self.downvotes -= 1
        self.save()
        return self.downvotes

    def __str__(self):
        return u'{0}/{1}'.format(self.upvotes, self.downvotes)


class AbstractThumbnail(models.Model):
    video = OneToOneField('videos.Video', primary_key=True,
                          related_name='thumbnail')
    url = models.CharField(max_length=255, default='', blank=True)
    width = models.PositiveIntegerField(default=0)
    height = models.PositiveIntegerField(default=0)

    def __str__(self):
        return u'{0}'.format(self.url)

    class Meta:
        abstract = True


class AbstractTag(models.Model):
    name = LowerCaseCharField(max_length=30,
                              unique=True,
                              validators=[Common.contains(constants.TAGS_ALLOWED_CHARACTERS)])
    objects = TagManager()

    def __str__(self):
        return self.name

    class Meta:
        abstract = True
