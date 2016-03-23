from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^users', include('users.urls_web', namespace='users')),
    #url(r'^/videos', include('videos.urls_web', namespace='videos')),
]
