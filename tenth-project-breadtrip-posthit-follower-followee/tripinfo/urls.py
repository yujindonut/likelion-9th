from django.urls import path, include
from django.urls.resolvers import URLPattern
from .views import *
from django.conf.urls import url, include

urlpatterns = [
    #게시글
    path('', home, name="home"),
    path('detail/<str:id>', detail, name="detail"),
    path('new/', new, name="new"),
    path('edit/<str:id>', edit, name="edit"),
    path('delete/<str:id>', delete, name="delete"),
    path('like/', post_likes, name="post_likes"),

    #댓글
    path('delete_comment/<str:post_id>/<str:comment_id>',
         delete_comment, name="delete_comment"),
    path('create_comment/<str:post_id>', create_comment, name="create_comment"),
    path('create_re_comment/<str:post_id>/<str:comment_id>',
         create_re_comment, name="create_re_comment"),
]
