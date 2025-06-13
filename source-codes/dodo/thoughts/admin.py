from django.contrib import admin
from .models import Folder, ToDo, Card

# Register your models here.
admin.site.register(Folder)
admin.site.register(ToDo)
admin.site.register(Card)