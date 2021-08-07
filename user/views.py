from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from community.models import *
from django.contrib.auth import get_user_model
# Create your views here.
from django.shortcuts import redirect, render,get_object_or_404
from django.contrib.auth.forms import AuthenticationForm,UserChangeForm
from django.contrib.auth import authenticate, login, logout
from .forms import *

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request,data = request.POST)
        if form.is_valid():#유효성 검사를 통과한 clean한 데이터중에 username이라는 것을 가져와서 변수에 저장
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            #user라는 객체를 만들 건데 이건 인증을 받는 객체임
            #form에서 받은 데이터들을 authenticate에 넣고 인증받는 거임
            user = authenticate(request=request,username=username,password=password)
            if user is not None:
                login(request,user)

        return redirect("index")
    else:
        form = AuthenticationForm()
        return render(request,'login.html',{'form':form})


def logout_view(request):
    logout(request)
    return redirect("index")

def register_view(request):
    if request.method =="POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()#얘는 commit없음
        return  redirect('index')
    else:
        form = SignUpForm()
        return render(request,'signUp.html',{'form':form})


    
def mypage(request):
    posts=Blog.objects.filter( writer = request.user).order_by('-id')
    comments=Comment.objects.filter( writer = request.user).order_by('-id')

    #posts=Blog.objects.all().order_by('-id')
    return render(request,'mypage.html',{'posts':posts,'comments':comments})
    


def editMypage(request):

    if request.method == "POST":
    	# updating
        user_change_form = CustomUserChangeForm(data=request.POST, instance=request.user)
        
        if user_change_form.is_valid() :
            user = user_change_form.save()
            return render(request,'mypage.html')
    else:
        # editting
        user_change_form = CustomUserChangeForm(instance=request.user)

        context = {
            'user_change_form': user_change_form,
        }
        
        return render(request, 'editMypage.html', context)
