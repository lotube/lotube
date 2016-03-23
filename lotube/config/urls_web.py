from django.conf.urls import include, url

urlpatterns = [
    url(r'^users', include('users.urls_web', namespace='users')),
    #url(r'^/videos', include('videos.urls_web', namespace='videos')),
]
