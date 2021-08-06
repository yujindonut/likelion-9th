from django.urls import path
from .views import *

urlpatterns = [
   path('',vaccine,name="vaccine"),
   
]