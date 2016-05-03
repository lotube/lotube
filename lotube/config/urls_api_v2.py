from rest_framework import routers

from videos.views_api_v2 import VideoAPIView, TagsAPIView
from users.views_api_v2 import UserAPIView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'videos/tags', TagsAPIView, base_name='videos-tags')
router.register(r'videos', VideoAPIView, base_name='videos')
router.register(r'users', UserAPIView, base_name='users')

urlpatterns = router.urls
