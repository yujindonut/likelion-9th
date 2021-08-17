from django.shortcuts import render, redirect, get_object_or_404 
from django.utils import timezone
from .models import *
from .forms import  *
from django.views.generic.edit import FormView
from django.db.models import Q
from django.core.paginator import Paginator

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
            return redirect('/fanclubpage/detail/' + str(id))
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
            comment.pub_date = timezone.now()
            comment.save()
    return redirect('/webtoonpage/detail/'+str(post_id))

#댓글삭제
def delete_comment(request,post_id,comment_id):
   deleteComment = get_object_or_404(Comment, pk=comment_id)
   deleteComment.delete() 
   return redirect("detail",post_id)    
