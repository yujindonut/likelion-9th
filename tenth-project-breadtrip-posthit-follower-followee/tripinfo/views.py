from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import *
from .forms import *
from django.views.generic.edit import FormView
from django.db.models import Q
from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import get_user_model
from datetime import date , datetime, timedelta
import json


def welcome(request):
    return render(request, 'welcome.html')


def home(request):
    blog_info = WriteInfoModel.objects.all().order_by('-id')
    comment_list = Comment.objects.all().order_by('-id')
    paginator = Paginator(blog_info, 5)
    paginatorComment = Paginator(comment_list, 5)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    Comments = paginatorComment.get_page(page)
    return render(request, 'home.html', {'posts': posts, 'commentList': Comments})


def detail(request, id):
    blog = get_object_or_404(WriteInfoModel, pk=id)
    comments = Comment.objects.filter(post_id=id, comment_id__isnull=True)
    re_comments = []
    for comment in comments:
        re_comments += list(Comment.objects.filter(comment_id=comment.id))
    commentForms = CommentForm()

    return render(request, 'detail.html', {'blog': blog, 'comments': comments, 're_comments': re_comments, 'commentForms': commentForms})


def new(request):
    if request.method == 'POST':
        form = InfoForm(request.POST, request.FILES)
        if form.is_valid():
            new_blog = form.save(commit=False)
            new_blog.writer = request.user
            new_blog.date = timezone.now()
            new_blog.save()
            return redirect('detail', new_blog.id)
        return redirect('home')
    else:
        form = InfoForm()
        return render(request, 'new.html', {'form': form})


def edit(request, id):
    update_blog = get_object_or_404(WriteInfoModel, pk=id)
    if request.method == 'POST':
        form = InfoForm(request.POST, request.FILES, instance=update_blog)
        if form.is_valid():
            update_blog = form.save(commit=False)
            update_blog.date = timezone.now()
            update_blog.save()
            return redirect('/tripinfo/detail/' + str(id))
        return redirect('home')
    else:  # Get??????
        form = InfoForm(instance=update_blog)
        return render(request, 'edit.html', {'form': form})

# ????????? ??????


def delete(request, id):
    delete = WriteInfoModel.objects.get(id=id)
    delete.delete()
    return redirect('home')

#????????????


def create_comment(request, post_id):
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post_id = WriteInfoModel.objects.get(pk=post_id)
            comment.pub_date = timezone.now()
            comment.writer = request.user
            comment.save()
    return redirect('/tripinfo/detail/'+str(post_id))

#???????????????


def create_re_comment(request, post_id, comment_id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post_id = WriteInfoModel.objects.get(pk=post_id)
            comment.comment_id = Comment.objects.get(pk=comment_id)
            comment.writer = request.user
            comment.pub_date = timezone.now()
            comment.save()
    return redirect('/tripinfo/detail/'+str(post_id))

#????????????


def delete_comment(request, post_id, comment_id):
   deleteComment = get_object_or_404(Comment, pk=comment_id)
   deleteComment.delete()
   return redirect("detail", post_id)

def post_likes(request):
  if request.is_ajax():  # ajax ????????? ??? ?????? ?????? ??????
    blog_id = request.GET['blog_id']  # ???????????? ?????? ?????????id (blog_id)????????? ??????
    post = WriteInfoModel.objects.get(id=blog_id)

    user = request.user  # request.user : ?????? ???????????? ??????
    if post.like.filter(id=user.id).exists():  # ?????? ???????????? ?????? ????????? ???
      post.like.remove(user)  # like field??? ?????? ?????? ??????
      message = "????????? ??????"  # ????????? ?????? ?????????
    else:  # ???????????? ????????? ?????? ????????? ???
      post.like.add(user)  # like field??? ?????? ?????? ??????
      message = "?????????"  # ????????? ?????? ?????????
    #post.like.count() : ???????????? ?????? ????????? ???
  context = {
      'like_count': post.like.count(),
      "message": message,
  }
  return HttpResponse(json.dumps(context), content_type='application/json')

