from django.conf.urls import include, url

urlpatterns = [
    url(r'^users', include('users.urls_api', namespace='users')),
    url(r'^/videos', include('videos.urls_api', namespace='videos')),
]
