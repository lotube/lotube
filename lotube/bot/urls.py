from django.conf.urls import include, url

from views import CrawlerBot

urlpatterns = [
    # CrawlerBot
    url(
        r'^launch',
        CrawlerBot().execute,
        name='CrawlerBot'
    ),

    # Crawler Management
    url(
        r'^manage',
        CrawlerBot().get_management,
        name='CrawlerManagement'
    )
]
