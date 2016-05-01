from django.contrib import admin
from .models import Video, Thumbnail, Analytic, Rating, Tag


class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created',)
    readonly_fields = ('show_url',)

    def show_url(self, instance):
        # TODO
        return 'http://.../' + instance.filename

    show_url.short_description = 'Filename URL'


class ThumbnailAdmin(admin.ModelAdmin):
    list_display = ('video', 'url')


class AnalyticAdmin(admin.ModelAdmin):
    list_display = ('video', 'views',)


class RatingAdmin(admin.ModelAdmin):
    list_display = ('video', 'upvotes', 'downvotes',)


admin.site.register(Video, VideoAdmin)
admin.site.register(Thumbnail, ThumbnailAdmin)
admin.site.register(Analytic, AnalyticAdmin)
admin.site.register(Rating, RatingAdmin)
admin.site.register(Tag)
