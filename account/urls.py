from django.urls import path
from .views import *

urlpatterns = [
    path('login/', login_view, name ="login"),
    path('logout/',logout_view, name="logout"),
    path('signup/',signup, name="signup"),
    path('mypage/',mypage,name="mypage"),
    path('follow/<int:pk>', follow, name='follow'),
    # path('followers/',followers,name="followers"),
]