from django.conf.urls import include, url

urlpatterns = [
    url(r'^api/', include('config.urls_api', namespace='api')),
    url(r'^', include('config.urls_web', namespace='web')),
]
