from django.db import models


class Track(models.Model):
    title = models.CharField(max_length=255)
    order = models.PositiveIntegerField()
    track_file = models.FileField(upload_to='tracks')
