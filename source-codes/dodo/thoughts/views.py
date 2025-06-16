from django.shortcuts import render, get_list_or_404
from .models import Folder, ToDo, Card


# Create your views here.
def index(request):
    folders = get_list_or_404(Folder, user=request.user)

    homeFolder = None
    for folder in folders:
        if folder.name=="Home":
            homeFolder = folder

    homeTodos = ToDo.objects.filter(folder_id=homeFolder.id)

    homeCards = Card.objects.filter(folder_id=homeFolder.id)

    return render(request, 'thoughts/index.html', {'folders': folders, 'homeTodos': homeTodos, 'homeCards': homeCards})

