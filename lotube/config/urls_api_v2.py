from django.conf.urls import include, url


urlpatterns = [
    url(r'^videos', include('videos.urls_api_v2')),
]
