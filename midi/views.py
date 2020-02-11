from django.shortcuts import render, get_object_or_404

from midi.models import Midi


def index(request):
    midi = Midi.objects.all()[:10]

    return render(request, 'midi/index.html', {
        'midi': midi,
    })


def view(request, pk):
    midi = get_object_or_404(Midi, pk=pk)

    return render(request, 'midi/view.html', {
        'midi': midi,
    })
