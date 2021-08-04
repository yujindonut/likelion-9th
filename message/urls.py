
from django.urls import path
from .views import *

urlpatterns = [
    
   path('', messageReception,name='messageReception'),
   path('sendMessage/',sendMessage,name='sendMessage'),
   path('newMessage/',newMessage,name='newMessage'),
    path('messageBox/',messageBox,name='messageBox'),
   path('detailMessage/<str:messageId>',detailMessage,name='detailMessage'),
]
