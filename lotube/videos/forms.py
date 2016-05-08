from django.forms import ModelForm
from models import *
from django import forms


class VideoEditForm(ModelForm):
    """
    A form for editing videos.
    """

    class Meta:
        model = Video
        fields = ('title', 'description',)
