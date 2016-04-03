import os
from django.http import HttpResponse

from lotube_crawler import Crawler
from videos.models import Video, Tag
from users.models import User


class CrawlerBot(object):

    def get_user(self):
        """
        Create Youtube user or return existing one
        :return: Youtube user
        """
        try:
            return User.objects.get(username='youtube')
        except User.DoesNotExist:
            user = User(
                username='youtube',
                email='youtube@crawlerbot.com'
            )
            user.set_password('youtube_bot')
            user.save()
            return user

    def get_tag(self, tag):
        """
        Creates Tag if it doesn't exist, else return existing one
        :param tag: tag name
        :return: Tag db object
        """
        try:
            return Tag.objects.get(name=tag)
        except Tag.DoesNotExist:
            tag = Tag(name=tag)
            tag.save()
            return tag

    def execute(self, request):
        token = os.environ.get('TOKEN_YOUTUBE')
        crawler = Crawler(site='youtube', site_token=token,
                          max_breadth=1, max_depth=1)
        for video in crawler.run(['games']):
            if Video.objects.filter(id_source=video.id_source).exists():
                continue

            base_url = 'http://www.youtube.com/watch?v='
            db_video = Video(id_source=video.id_source,
                             source='youtube',
                             user=self.get_user(),
                             title=video.title,
                             description=video.description,
                             filename=base_url+video.id_source)
            db_video.save()
            for tag in video.tags:
                db_video.tags.add(self.get_tag(tag))

        return HttpResponse('OK')
