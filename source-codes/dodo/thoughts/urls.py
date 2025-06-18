from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('<int:folder_id>/', views.folder, name="folder"),
    # Add Forms:
    path('folderform/', views.folderForm, name="folderform"),
    path('todoform/<int:folder_id>', views.todoForm, name="todoform"),
    path('cardform/<int:folder_id>', views.cardForm, name="cardform"),
    # Edit Forms:
    path('folderedit/<int:folder_id>/', views.folderEditForm, name="editfolderform"),
    path('todoedit/<int:todo_id>/', views.todoEditForm, name="edittodoform"),
    path('cardedit/<int:card_id>/', views.cardEditForm, name="editcardform"),
    # Delete Forms:
    path('folderdelete/<int:folder_id>/', views.folderDeleteForm, name="deletefolderform"),
    path('tododelete/<int:todo_id>/', views.todoDeleteForm, name="deletetodoform"),
    path('carddelete/<int:card_id>/', views.cardDeleteForm, name="deletecardform"),    
]