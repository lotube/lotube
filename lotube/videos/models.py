from __future__ import unicode_literals

from .abstract_models import AbstractVideo, AbstractAnalytic, AbstractTag, \
    AbstractRating, AbstractUpVote, AbstractDownVote


class Video(AbstractVideo):
    pass


class Analytic(AbstractAnalytic):
    pass


class Rating(AbstractRating):
    pass


class Tag(AbstractTag):
    pass


class UpVote(AbstractUpVote):
    pass


class DownVote(AbstractDownVote):
    pass
