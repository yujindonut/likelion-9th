from django.shortcuts import render, redirect, get_object_or_404 
from django.utils import timezone
from .models import *
from .forms import  *
from django.views.generic.edit import FormView
from django.db.models import Q
from django.core.paginator import Paginator
from django.http import HttpResponse,JsonResponse
import json

def welcome(request):
    return render(request, 'welcome.html')

def home(request):
    blog_info = WebtoonModel.objects.all() 
    paginator = Paginator(blog_info, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'home.html' , {'blog_info': blog_info, 'posts': posts})

def detail(request, id):
    blog = get_object_or_404(WebtoonModel,pk=id) 
    comments = Comment.objects.filter(post_id=id, comment_id__isnull=True)
    re_comments=[]
    for comment in comments:
        re_comments += list(Comment.objects.filter(comment_id=comment.id))
    commentForms = CommentForm()
    return  render(request,'detail.html',{'blog':blog,'comments':comments,'re_comments':re_comments,'commentForms':commentForms})

def new(request): 
    if request.method == 'POST' : 
        form = WebtoonForm(request.POST, request.FILES)
        if form.is_valid():
            new_blog = form.save(commit = False)
            new_blog.writer = request.user
            new_blog.date = timezone.now()
            new_blog.save()
            return redirect('detail', new_blog.id)
        return redirect('home')
    else: 
        form = WebtoonForm()  
        return render(request,'new.html', {'form' : form})

def edit(request,id):
    update_blog = get_object_or_404(WebtoonModel, pk = id)
    if request.method == 'POST': 
        form = WebtoonForm(request.POST, request.FILES, instance = update_blog)
        if form.is_valid():
            update_blog = form.save(commit = False)
            update_blog.date = timezone.now()
            update_blog.save()
            return redirect('/webtoonpage/detail/' + str(id))
        return redirect('home') 
    else: #Get방식
        form = WebtoonForm(instance = update_blog)
        return render(request, 'edit.html', {'form' : form})

# 게시글 삭제
def delete(request,id) :
    delete = WebtoonModel.objects.get(id = id)
    delete.delete()
    return redirect('home')      

def search(request):
    blogs = WebtoonModel.objects.all().order_by('-id')

    find = request.POST.get('find')

    if find:
        blogs = blogs.filter(webtoon_name__icontains=find)
        return render(request, 'search.html', {'blogs': blogs, 'find':find})
    else:
        return render(request, 'search.html')

#댓글작성
def create_comment(request, post_id):
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post_id = WebtoonModel.objects.get(pk = post_id)
            comment.pub_date = timezone.now()
            comment.writer = request.user
            comment.save()
    return redirect('/webtoonpage/detail/'+str(post_id))          

#대댓글작성
def create_re_comment(request, post_id, comment_id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post_id = WebtoonModel.objects.get(pk = post_id)
            comment.comment_id = Comment.objects.get(pk = comment_id)
            comment.writer = request.user
            comment.pub_date = timezone.now()
            comment.save()
    return redirect('/webtoonpage/detail/'+str(post_id))

#댓글삭제
def delete_comment(request,post_id,comment_id):
   deleteComment = get_object_or_404(Comment, pk=comment_id)
   deleteComment.delete() 
   return redirect("detail",post_id)    

def post_likes(request): 
  if request.is_ajax(): #ajax 방식일 때 아래 코드 실행
    blog_id = request.GET['blog_id'] #좋아요를 누른 게시물id (blog_id)가지고 오기
    post = WebtoonModel.objects.get(id=blog_id) 
    
    user = request.user #request.user : 현재 로그인한 유저
    if post.like.filter(id = user.id).exists(): #이미 좋아요를 누른 유저일 때
      post.like.remove(user) #like field에 현재 유저 추가
      message = "좋아요 취소" #화면에 띄울 메세지
    else: #좋아요를 누르지 않은 유저일 때
      post.like.add(user) #like field에 현재 유저 삭제
      message = "좋아요" #화면에 띄울 메세지
    #post.like.count() : 게시물이 받은 좋아요 수  
  context = {
    'like_count' : post.like.count(),
    "message":message,
  }
  return HttpResponse(json.dumps(context), content_type='application/json')  