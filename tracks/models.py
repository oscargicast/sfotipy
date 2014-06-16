from django.db import models
from django.utils.html import format_html


class Track(models.Model):
    title = models.CharField(max_length=255)
    order = models.PositiveIntegerField()
    track_file = models.FileField(upload_to='tracks')
    album = models.ForeignKey('albums.Album')
    artist = models.ForeignKey('artists.Artist')

    def get_absolute_url(self):
        return '/tracks/%s/' % self.title

    def player(self):
        return """
        <audio controls>
            <source src="%s" type="audio/mpeg">
            Your browser does not support the audio element.
        </audio>
        """ % self.track_file.url

    player.allow_tags = True
    player.admin_order_field = 'track_file'

    def __unicode__(self):
        return self.title
