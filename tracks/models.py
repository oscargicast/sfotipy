from django.db import models


class Track(models.Model):
    title = models.CharField(max_length=255)
    order = models.PositiveIntegerField()
    track_file = models.FileField(upload_to='tracks')
    album = models.ForeignKey('albums.Album')
    artist = models.ForeignKey('artists.Artist')

    def __unicode__(self):
        return self.title
