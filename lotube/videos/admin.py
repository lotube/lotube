from django.contrib import admin
from .models import Video, Analytic, Rating, Tag, Like


class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created',)


class AnalyticAdmin(admin.ModelAdmin):
    list_display = ('video', 'views',)


class RatingAdmin(admin.ModelAdmin):
    list_display = ('video', 'likes',)


class LikeAdmin(admin.ModelAdmin):
    list_display = ('rating', 'user')


admin.site.register(Video, VideoAdmin)
admin.site.register(Analytic, AnalyticAdmin)
admin.site.register(Rating, RatingAdmin)
admin.site.register(Like, LikeAdmin)
admin.site.register(Tag)
