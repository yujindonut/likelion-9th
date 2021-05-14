from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('<str:id>',detail,name="detail"),
    path('new/',new,name="new"),
    path('create/', create, name="createMine"), #create 
    path('edit/<str:id>', edit, name="editMine"), #edit
    path('update/<str:id>',update,name="updateMine"), #update
    path('delete/<str:id>',delete, name="deleteMine"), #delete
]
