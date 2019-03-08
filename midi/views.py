from django.shortcuts import render

from midi.models import Midi


def index(request):
    latest_midi = Midi.objects.all().order_by('-created_at')[:10]

    return render(request, 'midi/index.html', {
        'latest_midi': latest_midi,
    })
