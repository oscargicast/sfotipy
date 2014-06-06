from django.test import TestCase
from .models import Track
from artists.models import Artist
from albums.models import Album


class TrackTestCase(TestCase):
    def setUp(self):
        self.artist = Artist.objects.create(
            first_name="beyonce",
            last_name="giselle knowles",
            biography="American singer and actress...",
        )
        self.album = Album.objects.create(
            title="Love Songs",
            artist=self.artist,
        )
        self.track = Track.objects.create(
            title="xo",
            order=15,
            album=self.album,
            artist=self.artist,
        )

    def test_track(self):
        self.assertEqual(self.track.title, "xo")
        self.assertEqual(self.track.album.title, "Love Songs")
