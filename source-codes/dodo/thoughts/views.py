from django.shortcuts import render, get_list_or_404, redirect
from .models import Folder, ToDo, Card
from .forms import AddFolderForm, AddToDoForm, AddCardForm

def getHomeFolder():
    pass

# thoughts/index.html
def index(request):
    folders = get_list_or_404(Folder, user=request.user)

    homeFolder = None
    for folder in folders:
        if folder.name=="Home":
            homeFolder = folder

    homeTodos = ToDo.objects.filter(folder_id=homeFolder.id)

    homeCards = Card.objects.filter(folder_id=homeFolder.id)

    return render(request, 'thoughts/index.html', {'folders': folders, 'homeTodos': homeTodos, 'homeCards': homeCards})

# thoughts/folder_id
def folder(request, folder_id):
    todos = ToDo.objects.filter(folder_id=folder_id)
    cards = Card.objects.filter(folder_id=folder_id)

    return render(request, 'thoughts/folder.html', {'todos': todos, 'cards': cards, 'folder_id': folder_id})

def folderForm(request):
    if request.method == "POST":
        form = AddFolderForm(request.POST)
        print(form)
        if form.is_valid():
            folder = form.save(commit=False)
            folder.user = request.user
            folder.save()
            return redirect('index')
    else:
        form = AddFolderForm()
    return render(request, 'thoughts/folderForm.html', {'form': form})

def todoForm(request, folder_id):

    if request.method == "POST":
        form = AddToDoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.folder_id = folder_id
            todo.save()
            return redirect('index')
    else:
        form = AddToDoForm()
        
    return render(request, 'thoughts/todoForm.html', {'form': form})

def cardForm(request):
    form = AddFolderForm()
    return render(request, 'thoughts/cardForm.html', {'form': form})