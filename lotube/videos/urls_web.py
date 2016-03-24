from django.conf.urls import url

from .views_web import VideoList, VideoDetail

urlpatterns = [
    #List of Videos
    url(
        r'^$',
       VideoList.as_view(),
        name='videos'
    ),

    #Retrieve a specific Video
    url(
        r'^\/(?P<pk>)$',
        VideoDetail.as_view(),
        name='video'
    ),
]
