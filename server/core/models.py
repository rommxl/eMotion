from django.db import models

# Create your models here.
class Video(models.Model):
    video_file = models.FileField(null=True, blank=True, upload_to='videos/')