from django.urls import path, include
from django.urls.resolvers import URLPattern
from .views import *
from django.conf.urls import url, include


urlpatterns = [
    path('receive_message', receive_message, name = "receive_message"),
    path('send_message', send_message, name = "send_message"),
    path('detail_message/<str:id>', detail_message, name="detail_message"),
    path('new_message/', new_message, name="new_message"),
    path('edit_message/<str:id>', edit_message, name="edit_message"),
    path('delete_message/<str:id>',delete_message, name="delete_message"),
]