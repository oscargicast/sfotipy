from django.test import TestCase
from .models import Artist

class ArtistTestCase(TestCase):
    def setUp(self):
        Artist.objects.create(
            first_name="oscar",
            last_name="giraldo",
            biography="mechatronics engineering student",
        )

    def test_artist(self):
        oscar = Artist.objects.get(first_name="oscar")
        self.assertEqual(oscar.first_name, "oscar")
        self.assertEqual(oscar.last_name, "giraldo")
