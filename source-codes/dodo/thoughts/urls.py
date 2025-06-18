from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('folderform/', views.folderForm, name="folderform"),
    path('todoform/<int:folder_id>', views.todoForm, name="todoform"),
    path('cardform/<int:folder_id>', views.cardForm, name="cardform"),
    path('<int:folder_id>/', views.folder, name="folder"),
]