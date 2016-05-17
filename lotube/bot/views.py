import os
import threading

from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect

from lotube_crawler import Crawler
from videos.models import Video, Tag
from users.models import User

from lotube.bot.forms import CrawlerForm


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class CrawlerBot(object):
    __metaclass__ = Singleton

    def __init__(self):
        # Threading control
        self.threads = {}

        self.mutex = threading.Lock()

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

    def get_threads(self):
        self.mutex.acquire()
        num = len(self.threads)
        self.mutex.release()
        return num

    def execute(self, request):
        if not request.user.is_authenticated() or not request.user.is_staff:
            raise PermissionDenied

        if request.method == 'POST':
            form = CrawlerForm(request.POST)
            if form.is_valid():
                term = form.cleaned_data['term']
                max_depth = form.cleaned_data['max_depth']
                max_breadth = form.cleaned_data['max_breadth']
                args = [term, max_depth, max_breadth]
                # Threading _execute_crawler function
                t = threading.Thread(target=self._execute_crawler,
                                     args=args)
                t.setDaemon(True)
                t.start()
                self.mutex.acquire()
                self.threads[t.ident] = args
                self. mutex.release()
                return redirect('/bot/manage')
        else:
            form = CrawlerForm()
        return render(request, 'bot/bot.html', {'form': form, 'nthreads': self.get_threads()})

    def get_management(self, request):
            self.mutex.acquire()
            response = render(request, 'bot/bot_management.html',
                              {'threads': self.threads, 'nthreads': len(self.threads)})
            self. mutex.release()
            return response

    def _execute_crawler(self, term, max_depth, max_breadth):
        token = os.environ.get('TOKEN_YOUTUBE')
        crawler = Crawler(site='youtube', site_token=token,
                          max_breadth=max_breadth, max_depth=max_depth)
        for video in crawler.run(term.split()):
            if Video.objects.filter(id_source=video.id_source).exists():
                continue

            base_url = 'http://www.youtube.com/watch?v='
            db_video = Video(id_source=video.id_source,
                             source='youtube',
                             user=self.get_user(),
                             title=video.title,
                             description=video.description,
                             filename=base_url+video.id_source)
            db_video.save(force_insert=True)  # Could be problematic on sqlite
            for tag in video.tags:
                db_video.tags.add(self.get_tag(tag))

        # Erase CrawlerBot thread controller
        self.mutex.acquire()
        del(self.threads[threading.currentThread().ident])
        self.mutex.release()
