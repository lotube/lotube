from rest_framework import routers

from videos.comments.views_api_v2 import CommentAPIView
from videos.views_api_v2 import VideoAPIView, TagAPIView, LikeAPIView
from users.views_api_v2 import UserAPIView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'videos/(?P<video>\d+)/comments', CommentAPIView,
                base_name='video-comments')
router.register(r'videos/(?P<video>\d+)/likes', LikeAPIView,
                base_name='video-likes')
router.register(r'videos/tags', TagAPIView, base_name='videos-tags')
router.register(r'videos', VideoAPIView, base_name='videos')
router.register(r'users', UserAPIView, base_name='users')

urlpatterns = router.urls
