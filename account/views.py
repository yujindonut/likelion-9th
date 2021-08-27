from django.shortcuts import render, redirect, get_object_or_404 
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm
from tripinfo.models import *
from .forms import *

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request= request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username") #cleaned_data:유효성 검사에 성공한 데이터
            password = form.cleaned_data.get("password")
            user = authenticate(request = request, username = username, password = password)
            if user is not None: #user가 존재할 때
                login(request, user)
        return redirect("home")
    else:
        form = AuthenticationForm()
        return render( request, 'login.html', {'form':form} )

def logout_view(request):
    logout(request)
    return redirect("home")

def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
        return redirect("home")
    
    else:
        signup_form = SignUpForm()
        return render(request, 'signup.html', {'signup_form':signup_form})

def mypage(request):
    
    comments=Comment.objects.filter( writer = request.user).order_by('-id')
    
    paginatorComment = Paginator(comments, 5)
    page = request.GET.get('page')
    
    Comments = paginatorComment.get_page(page)
    return render(request, 'mypage.html', {'commentList': Comments})

# def followers(request):

#     followings = request.user.followings.all()
#     posts = WriteInfoModel.objects.filter(writer__in = followings).order_by('id')
#     page = request.GET.get('page')
    
#     paginator = Paginator(posts, 5)
#     posts = paginator.get_page(page)

#     return render(request, 'followers.html', {'posts': posts})

def follow(request, pk):
    User = get_user_model()
    # 팔로우 당하는 사람
    user = get_object_or_404(User, id=pk)
    # if user.followers.filter(pk=request.user.pk).exists():
    if request.user in user.followers.all():
        user.followers.remove(request.user)
    else:
        user.followers.add(request.user)
    return redirect("home")
