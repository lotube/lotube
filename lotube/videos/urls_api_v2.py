from django.conf.urls import url, include
from rest_framework import routers

from videos.views_api_v2 import VideosListView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'videos', VideosListView)

urlpatterns = [
    url('^\/', include(router.urls))
]
