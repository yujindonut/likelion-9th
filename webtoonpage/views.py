from datetime import time
from django.core import paginator
from django.shortcuts import render, redirect, get_object_or_404 
from django.utils import timezone
from .models import WebtoonModel
from .forms import WebtoonForm
from django.core.paginator import Paginator
from django.core.mail import EmailMessage

def welcome(request):
    return render(request, 'welcome.html')

def home(request):
    blog_info = WebtoonModel.objects.all() 
    paginator = Paginator(blog_info, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'home.html' , {'blog_info': blog_info, 'posts': posts})

def detail(request, id):
    blog_info = get_object_or_404(WebtoonModel, pk = id)
    return render(request, 'detail.html', {'blog_info': blog_info})

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
