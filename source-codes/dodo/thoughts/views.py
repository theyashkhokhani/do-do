from django.shortcuts import render, get_list_or_404, redirect, get_object_or_404
from .models import Folder, ToDo, Card
from .forms import AddFolderForm, AddToDoForm, AddCardForm

def getHomeFolder():
    pass

# thoughts/index.html
def index(request):
    folders = get_list_or_404(Folder, user=request.user)

    # removed home folder from the folder's list as we are showing the content of the home folder on thoughts/index route.
    counter = 0
    homeFolder = None
    for folder in folders:
        if folder.name=="Home":
            homeFolder = folder
            break
        counter += 1
    folders.pop(counter)

    homeTodos = ToDo.objects.filter(folder_id=homeFolder.id)
    homeCards = Card.objects.filter(folder_id=homeFolder.id)

    return render(request, 'thoughts/index.html', {'folders': folders, 'homeTodos': homeTodos, 'homeCards': homeCards,  'homeFolder': homeFolder})

# thoughts/folder_id
def folder(request, folder_id):
    todos = ToDo.objects.filter(folder_id=folder_id)
    cards = Card.objects.filter(folder_id=folder_id)

    return render(request, 'thoughts/folder.html', {'todos': todos, 'cards': cards, 'folder_id': folder_id})

# folderform
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

def cardForm(request, folder_id):
    if request.method == "POST":
        form = AddCardForm(request.POST)
        if form.is_valid():
            card = form.save(commit=False)
            card.folder_id = folder_id
            card.save()
            return redirect('index')
    else:
        form = AddCardForm()
    return render(request, 'thoughts/cardForm.html', {'form': form})

def folderEditForm(request, folder_id):
    folder = get_object_or_404(Folder, pk=folder_id)
    if request.method == "POST":
        form = AddFolderForm(request.POST, instance=folder)
        if form.is_valid():
            folder = form.save(commit=False)
            # folder.user = request.user
            folder.save()
            return redirect('index')
    else:
        form = AddFolderForm(instance=folder)
    return render(request, 'thoughts/folderForm.html', {'form': form})

def todoEditForm(request, todo_id):
    todo = get_object_or_404(ToDo, pk=todo_id)
    if request.method == "POST":
        form = AddToDoForm(request.POST, instance=todo)
        if form.is_valid():
            todo = form.save(commit=False)
            # todo.folder = request.folder
            todo.save()
            return redirect('index')
    else:
        form = AddToDoForm(instance=todo)
    return render(request, 'thoughts/todoForm.html', {'form': form})

def cardEditForm(request, card_id):
    card = get_object_or_404(Card, pk=card_id)
    if request.method == "POST":
        form = AddCardForm(request.POST, instance=card)
        if form.is_valid():
            card = form.save(commit=False)
            # card.folder = request.folder
            card.save()
            return redirect('index')
    else:
        form = AddCardForm(instance=card)
    return render(request, 'thoughts/cardForm.html', {'form': form})

def folderDeleteForm(request, folder_id):
    folder = get_object_or_404(Folder, pk=folder_id, user=request.user)
    if request.method == "POST":
        folder.delete()
        return redirect('index')
    return render(request, 'thoughts/folderDeleteConfirm.html', {'folder': folder})

def todoDeleteForm(request, todo_id):
    todo = get_object_or_404(ToDo, pk=todo_id)
    if request.method == "POST":
        todo.delete()
        return redirect('index')
    return render(request, 'thoughts/todoDeleteConfirm.html', {'todo': todo})

def cardDeleteForm(request, card_id):
    card = get_object_or_404(Card, pk=card_id)
    if request.method == "POST":
        card.delete()
        return redirect('index')
    return render(request, 'thoughts/cardDeleteConfirm.html', {'card': card})

