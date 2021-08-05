
from django.urls import path
from .views import *

urlpatterns = [
    
   path('', messageReception,name='messageReception'),
   path('sendMessage/',sendMessage,name='sendMessage'),
   path('sendToMe/',sendToMe,name='sendToMe'),
   path('newMessage/',newMessage,name='newMessage'),
   path('newMessageToMe/',newMessageToMe,name='newMessageToMe'),
   path('messageBox/',messageBox,name='messageBox'),
   path('detailMessage/<str:messageId>',detailMessage,name='detailMessage'),
   path('deleteMessage/<str:messageId>',deleteMessage,name='deleteMessage'),
]
