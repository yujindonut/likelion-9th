from django.urls import path, include
from django.urls.resolvers import URLPattern
from .views import *

urlpatterns = [
    path('', home, name = "home"),
    path('detail/<str:id>', detail, name="detail"),
    path('new/', new, name="new"),
    path('edit/<str:id>', edit, name="edit"),
    path('delete/<str:id>',delete, name="delete"),
    path('search', search, name='search'),
]