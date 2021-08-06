from django.urls import path
from .views import *

urlpatterns = [
   #게시글
   path('detailPage/<str:postId>',detail,name="detailPage"),
   path('newPost/',new,name="newPost"),
   path('editPost/<str:postId>',edit,name="editPost"),
   path('deletePost/<str:postId>',delete,name="deletePost"),

#게시판 카테고리

   path('allPost/', allPost,name="allPost"), #이거 전체 게시판임
   path('pre10/',pre10,name="pre10"),
   path('y10/',y10,name="y10"),
   path('y20/',y20,name="y20"),
   path('y30_40/',y30_40,name="y30_40"),
   path('y50_60/',y50_60,name="y50_60"),
   path('over70/',over70,name="over70"),
   
   path('moderna/',moderna,name="moderna"),
   path('pfizer/',pfizer,name="pfizer"),
   path('az/',az,name="az"),
   path('janssen/',janssen,name="janssen"),
   path('free/',free,name="free"),

   #댓글
   path('deleteComment/<str:postId>/<str:commentId>',deleteComment,name="deleteComment"),
   path('update_review/<str:post_id>/<str:comment_id>', update_review, name="update_review"),
   path('create_comment/<str:postId>',create_comment,name="create_comment"),
   path('create_re_comment/<str:postId>/<str:comment_id>',create_re_comment,name="create_re_comment"),
   

   #검색
   path('search/', SearchFormView.as_view(), name='search'),

#홈페이지
   path('allPost/', allPost, name='allPost'),

   
]