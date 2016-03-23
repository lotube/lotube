from django.contrib import admin
from .models import Video, VideoAnalytic, Comment, Tag


class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created')


class CommentAdmin(admin.ModelAdmin):
    pass

admin.site.register(Video, VideoAdmin)
admin.site.register(VideoAnalytic)
admin.site.register(Comment)
admin.site.register(Tag)
