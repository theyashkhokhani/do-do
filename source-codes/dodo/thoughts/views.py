from django.shortcuts import render, get_list_or_404
from .models import Folder, ToDo, Card

# Create your views here.
def index(request):
    folders = Folder.objects.filter()
    # print(folders)
    todos = ToDo.objects.filter()
    cards = Card.objects.filter()

    return render(request, 'thoughts/index.html', {'folders': folders, 'todos': todos, 'cards': cards})

