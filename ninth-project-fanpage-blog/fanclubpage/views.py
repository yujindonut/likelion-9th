from datetime import time
from django.core import paginator
from django.shortcuts import render, redirect, get_object_or_404 
from django.utils import timezone
from .models import unnie_info
from .forms import UnnieInfoForm
from django.core.paginator import Paginator
from django.core.mail import EmailMessage

def welcome(request):
    return render(request, 'welcome.html')

def home(request):
    blog_info = unnie_info.objects.all() 
    #models.py의 데이터들을 가져온다
    #블로그 모든 글들을 대상으로
    #블로그 객체 세개를 한페이지로 자르기
    paginator = Paginator(blog_info, 3)
    #request된 페이지가 뭔지를 알아내고 (request페이지를 변수에 담아내고)
    page = request.GET.get('page')
    #request된 페이지를 얻어온 뒤 return 해준다
    posts = paginator.get_page(page)
    return render(request, 'home.html' , {'blog_info': blog_info, 'posts': posts})

def detail(request, id):
    blog_info = get_object_or_404(unnie_info, pk = id)
    return render(request, 'detail.html', {'blog_info': blog_info})

def new(request): 
    if request.method == 'POST' : #글을 작성한 후 저장 버튼을 눌렀을 때 = 파라미터로 받은게 있을때
        form = UnnieInfoForm(request.POST, request.FILES)
        if form.is_valid():
            new_blog = form.save(commit = False)
            new_blog.date = timezone.now()
            new_blog.save()
            return redirect('detail', new_blog.id)
            #유효성 검사에 성공해서 글을 작성하면 detail로 가게
        return redirect('home')
    else: 
        form = UnnieInfoForm() #글을 입력받기 위한 빈 form을 불러온다  
        return render(request,'new.html', {'form' : form})

def edit(request,id):
    update_blog = get_object_or_404(unnie_info, pk = id)
    if request.method == 'POST': #update #글을 수정하고 수정버튼을 눌렀을 때
        form = UnnieInfoForm(request.POST, request.FILES, instance = update_blog)
        #현재 post에 가져온 정보를 form에 담는다
        if form.is_valid():
            update_blog = form.save(commit = False)
            update_blog.date = timezone.now()
            update_blog.save()
            return redirect('/fanclubpage/detail/' + str(id))#글이 저장되었으면 detail페이지  
        return redirect('home') #가져온정보가 유효하지 않을 때 home으로 가게
    else: #Get방식
        form = UnnieInfoForm(instance = update_blog)
        return render(request, 'edit.html', {'form' : form})
        #수정된 정보를 edit.html에 보내준다.

def delete(request,id) :
    delete = unnie_info.objects.get(id = id)
    delete.delete()
    return redirect('home')      

def search(request):
    blogs = unnie_info.objects.all().order_by('-id')
    #모든 객체를 id의 역순으로 담는다

    find = request.POST.get('find', "")

    if find:
        #음식장르로 검색
        blogs = blogs.filter(subject__icontains=find)
        #Post로 넘어온 값 비교
        return render(request, 'search.html', {'blogs': blogs, 'find':find})
    else:
        return render(request, 'search.html')
