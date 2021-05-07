from django.contrib import admin
from django.urls import path
from mediaformBlog.views import *

urlpatterns = [
    path('<str:id>',detailMedia,name="detailMedia"),
    path('new/',newMedia,name="newMedia"),
    path('create/', createMedia, name="createMedia"), 
    path('edit/<str:id>', editMedia, name="editMedia"), 
    path('update/<str:id>', updateMedia ,name="updateMedia"), 
    path('delete/<str:id>', deleteMedia , name="deleteMedia"), 
]
