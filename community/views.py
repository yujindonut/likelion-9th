from django.shortcuts import render,redirect,get_object_or_404
from .models import Blog
from django.utils import timezone
from .forms import BlogForm
# Create your views here.
def home(request):
    posts=Blog.objects.all()
    return render(request,"home.html",{'blogContents':posts})

def detail(request,postId):
    post = get_object_or_404(Blog,pk=postId) 
    return  render(request,'detail.html',{'postContents':post})

def new(request):
    if request.method == 'POST': #글 작성 후 저장버튼 눌렀을 때
        post_form = BlogForm(request.POST,request.FILES)
        if post_form.is_valid():# 이 form을 유효한지 검사후 유효하면 save해줌 (임시저장)
            post = post_form.save(commit = False)#임시저장 해주는 이유는 model에 있는 필드 중 new date를 안 담았음 (commit=False)
            post.writer = request.user
            post.pub_date = timezone.now() 
            post.save()
            return redirect("detailPage",post.id)
    else:
        post_form = BlogForm()
        return render(request,'new.html',{'form':post_form})

def edit(request,postId):
    post = get_object_or_404(Blog,pk=postId)
    if request.method == 'GET': #수정
        post_form=BlogForm(instance=post)
        return render(request,'edit.html',{'edit_post':post_form})
    else:
        post_form = BlogForm(request.POST,request.FILES,instance = post)
        if post_form.is_valid():
            post = post_form.save(commit = False)
            post.new_date = timezone.now() # 날짜 생성
            post.save()
        return redirect("detailPage",post.id)

def delete(request,postId):
   deletePost = get_object_or_404(Blog,pk=postId)
   deletePost.delete() #삭제해주는 메소드
   return redirect('home')