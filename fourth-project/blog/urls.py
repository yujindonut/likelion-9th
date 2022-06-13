from django.contrib import admin
from django.urls import path
from .views import *
#blog안에 있기 때문에 blog.views이렇게 안써도 됨

urlpatterns = [
    #데이터베이스의 id값에 따라 페이지가 다르게 보이고 view.py에 매개변수로 들어가기도 함
    path('<str:id>',detail,name="detail"),
    path('new/',new,name="new"),
    path('create/', create, name="createMine"), #create 
    path('edit/<str:id>', edit, name="editMine"), #edit
    #id값을 매개변수로 받기 때문에 path converter를 사용해야한다.
    #views.py에서 매개변수를 받고 싶을 때, 경로에 pathconverter를 사용해야한다. --> html의 url부분에도 경로와 id 모두 써줘야함
    path('update/<str:id>',update,name="updateMine"), #update
    path('delete/<str:id>',delete, name="deleteMine"), #delete
]
