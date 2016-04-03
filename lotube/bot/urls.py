from django.conf.urls import include, url

from views import CrawlerBot

urlpatterns = [
    # CrawlerBot
    url(
        r'^CrawlerBot',
        CrawlerBot().execute,
        name='CrawlerBot'
    ),
]
