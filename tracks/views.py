import json
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Track


def track_view(request, title):
    track = get_object_or_404(Track, title=title)
    data = {
        'title': track.title,
        'order': track.order,
        'album': track.album.title,
        'artist': {
            'name': track.artist.first_name,
            'bio': track.artist.biography,
        }
    }
    json_data = json.dumps(data)

    return HttpResponse(json_data, content_type='application/json')
