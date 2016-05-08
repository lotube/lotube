from django.forms import ModelForm
from models import *


class VideoEditForm(ModelForm):
    """
    A form for editing videos.
    """

    class Meta:
        model = Video
        fields = ('title', 'description', 'thumbnail',)
