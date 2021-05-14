from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('detail/<str:id>',detailMedia,name="detailMedia"),
    path('new/',newMedia,name="newMedia"),
    # path('create/', newMedia, name="createMedia"), 
    path('edit/<str:id>', editMedia, name="editMedia"), 
    # path('update/<str:id>', editMedia ,name="updateMedia"), 
    path('delete/<str:id>', deleteMedia , name="deleteMedia"), 
]
