from django.urls import path
from .views import *

urlpatterns = [
    path('login/',login_view,name="login"),
    path('logout/',logout_view,name="logout"),
    path('signUp/',register_view,name="signUp"),
    path('myPage/',myPage,name="myPage"),
    #path('editMyPage/',editMyPage,name="editMyPage"),
]