from rest_framework import routers

from videos.views_api_v2 import VideoAPIView, TagsAPIView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'videos/tags', TagsAPIView, base_name='videos-tags')
router.register(r'videos', VideoAPIView, base_name='videos')

urlpatterns = router.urls
