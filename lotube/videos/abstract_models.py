from django.db import models

from core.models import LowerCaseCharField
from core.validators import Common
from users.models import User


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
    analytic = models.OneToOneField('videos.VideoAnalytic',
                                    on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        abstract = True


class AbstractVideoAnalytic(models.Model):
    views = models.PositiveIntegerField(default=0)

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
    video = models.ForeignKey('videos.Video', on_delete=models.CASCADE)
    tag = LowerCaseCharField(max_length=30,
                             validators=[Common.contains('a-z0-9+#-.')])

    def __str__(self):
        return self.tag

    class Meta:
        abstract = True
