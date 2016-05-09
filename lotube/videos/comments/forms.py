from django import forms
from models import *
from django.forms import ModelForm


class CommentAddForm(ModelForm):

    class Meta:
        model = Comment
        fields = ['content']
