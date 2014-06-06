from django.test import TestCase
from .models import Album
from artists.models import Artist


class AlbumTestCase(TestCase):
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

    def test_album(self):
        self.assertEqual(self.album.title, "Love Songs")
        self.assertEqual(self.album.artist.first_name, "beyonce")
