from django.contrib import admin
from .models import Video, Analytic, Tag


class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created',)
    readonly_fields = ('show_url',)

    def show_url(self, instance):
        # TODO
        return 'http://.../' + instance.filename

    show_url.short_description = 'Filename URL'


class AnalyticAdmin(admin.ModelAdmin):
    list_display = ('video', 'views',)


admin.site.register(Video, VideoAdmin)
admin.site.register(Analytic, AnalyticAdmin)
admin.site.register(Tag)
