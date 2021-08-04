from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm

# Create your views here.
from django.shortcuts import redirect, render,get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm

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

        return redirect("home")
    else:
        form = AuthenticationForm()
        return render(request,'login.html',{'form':form})


def logout_view(request):
    logout(request)
    return redirect("home")

def register_view(request):
    if request.method =="POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()#얘는 commit없음
        return  redirect('home')
    else:
        form = SignUpForm()
        return render(request,'signUp.html',{'form':form})

def editMyPage(request):
    if request.method =="GET":
        form = SignUpForm()
        return render(request,'editMyPage.html',{'userform':form})
    else:
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
        return  redirect('myPage')
        

    
def myPage(request):
    if request.method == 'GET':
        form = AuthenticationForm()
        return render(request,'myPage.html',{'form':form})