from django.contrib import admin
from .models import Video, Analytic, Comment, Tag


class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created',)
    readonly_fields = ('show_url',)

    def show_url(self, instance):
        # TODO
        return 'http://.../' + instance.filename

    show_url.short_description = 'Filename URL'


class AnalyticAdmin(admin.ModelAdmin):
    list_display = ('video', 'views',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('content_shortener', 'video', 'user',)

    def content_shortener(self, instance):
        content = instance.content
        return content if len(content) < 30 else content[:30] + '...'

    content_shortener.short_description = 'Content'


admin.site.register(Video, VideoAdmin)
admin.site.register(Analytic, AnalyticAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Tag)
