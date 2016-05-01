from __future__ import unicode_literals

from django.apps import AppConfig


class VideosConfig(AppConfig):
    name = 'videos'

    def ready(self):
        from . import signals
