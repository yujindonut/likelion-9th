from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm

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

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
        return redirect("home")
    else:
        form = RegisterForm()
        return render( request, 'signup.html', {'form':form} )
