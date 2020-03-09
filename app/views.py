from django.shortcuts import render, get_object_or_404

from app.models import Midi


def index(request):
    midi = Midi.objects.all()[:10]

    return render(request, 'app/index.html', {
        'midi': midi,
    })


def view(request, pk):
    midi = get_object_or_404(Midi, pk=pk)

    return render(request, 'app/view.html', {
        'midi': midi,
    })
