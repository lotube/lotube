from django.forms import ModelForm

from models import *


class VideoCreateForm(ModelForm):
    """
    A form for creating videos.
    """

    class Meta:
        model = Video
        fields = ('title', 'description', 'filename', 'thumbnail',)


class VideoEditForm(ModelForm):
    """
    A form for editing videos.
    """

    class Meta:
        model = Video
        fields = ('title', 'description', 'filename', 'thumbnail',)
