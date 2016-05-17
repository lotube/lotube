import os
import threading

from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.shortcuts import render

from lotube_crawler import Crawler
from videos.models import Video, Tag
from users.models import User

from lotube.bot.forms import CrawlerForm


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
        if not request.user.is_authenticated() or not request.user.is_staff:
            raise PermissionDenied

        if request.method == 'POST':
            form = CrawlerForm(request.POST)
            if form.is_valid():
                term = form.cleaned_data['term']
                max_depth = form.cleaned_data['max_depth']
                max_breadth = form.cleaned_data['max_breadth']
                # Threading _execute_crawler function
                t = threading.Thread(target=self._execute_crawler,
                                     args=[term, max_depth, max_breadth])
                t.setDaemon(True)
                t.start()
                return HttpResponse('OK')
        else:
            form = CrawlerForm()

        return render(request, 'bot/bot.html', {'form': form})

    def _execute_crawler(self, term, max_depth, max_breadth):
        token = os.environ.get('TOKEN_YOUTUBE')
        crawler = Crawler(site='youtube', site_token=token,
                          max_breadth=max_breadth, max_depth=max_depth)
        for video in crawler.run(term.split()):  # Test with split()
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

        # if not request.user.is_authenticated() or not request.user.is_staff:
        #     raise PermissionDenied
        # token = os.environ.get('TOKEN_YOUTUBE')
        # crawler = Crawler(site='youtube', site_token=token,
        #                   max_breadth=1, max_depth=1)
        # for video in crawler.run(['games']):
        #     if Video.objects.filter(id_source=video.id_source).exists():
        #         continue
        #
        #     base_url = 'http://www.youtube.com/watch?v='
        #     db_video = Video(id_source=video.id_source,
        #                      source='youtube',
        #                      user=self.get_user(),
        #                      title=video.title,
        #                      description=video.description,
        #                      filename=base_url+video.id_source)
        #     db_video.save()
        #     for tag in video.tags:
        #         db_video.tags.add(self.get_tag(tag))
        #
        # return HttpResponse('OK')
