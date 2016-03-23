from __future__ import unicode_literals

from django.db import models
from .abstract_models import AbstractVideo, AbstractVideoAnalytic
from .abstract_models import AbstractComment, AbstractTag


class Video(AbstractVideo):
    pass


class VideoAnalytic(AbstractVideoAnalytic):
    pass


class Tag(AbstractTag):
    pass


class Comment(AbstractComment):
    pass
