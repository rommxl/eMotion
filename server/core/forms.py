from django import forms
from .models import Video
from django.forms import ModelForm

class UploadVideoForm(ModelForm):
    class Meta:
        model = Video
        fields = ('video_file',)
        labels = {
            'video_file':'',
        }