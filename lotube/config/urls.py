from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.views.generic import RedirectView

from config import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^bot/', include('bot.urls')),
    url(r'^api/v1/', include('config.urls_api', namespace='api')),
    url(r'^api/v2/', include('config.urls_api_v2', namespace='api_v2')),
    url(r'^', include('config.urls_web', namespace='web')),
    url(r'^$', RedirectView.as_view(url='videos'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
