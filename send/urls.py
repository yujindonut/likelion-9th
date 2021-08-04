from django.urls import path, include
from .views import *


urlpatterns = [
    path('', base, name = "base"),
    path('sendmail/', sendmail, name = "sendmail"),
]