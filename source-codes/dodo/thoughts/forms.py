from django import forms
from django.shortcuts import get_list_or_404
from django.forms import ModelForm
from .models import Folder, ToDo, Card

class AddFolderForm(ModelForm):
    class Meta:
        model = Folder
        fields = ['name']

class AddToDoForm(ModelForm):
    class Meta:
        model = ToDo
        fields = ['tag', 'description', 'status']

class AddCardForm(ModelForm):
    class Meta:
        model = Card
        fields = ['title', 'description']