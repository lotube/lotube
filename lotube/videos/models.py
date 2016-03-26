from __future__ import unicode_literals

from .abstract_models import AbstractVideo, AbstractAnalytic
from .abstract_models import AbstractComment, AbstractTag


class Video(AbstractVideo):
    pass


class Analytic(AbstractAnalytic):
    pass


class Tag(AbstractTag):
    pass


class Comment(AbstractComment):
    pass
