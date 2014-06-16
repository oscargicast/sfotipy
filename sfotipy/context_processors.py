from random import choice
from tracks.models import Track


frases = ['lol', 'hola', 'ke', 'ase']


def basic(request):
    tracks = Track.objects.all()
    track = None
    for t in tracks:
        if request.path == t.get_absolute_url():
            track = t
            break

    return {
        'titulo': choice(frases),
        'tracks': tracks,
        'selected_track': track,
    }
