from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('config.urls_api', namespace='api')),
    url(r'^', include('config.urls_web', namespace='web')),
]
