from django.shortcuts import render, get_object_or_404 #알 수 없는 페이지를 가져오라고 했을때 404Error를 처리한다.
from .models import Blog #데이터베이스에서 Blog에 대한 정보를 다가져온다
# Create your views here.

def FirstPage(request) : #home
    blogInfo = Blog.objects.all() #blogs
    return render(request,'home.html',{'blogInfo' : blogInfo })

def detail(request,id) : #detail
    blogInformation = get_object_or_404(Blog, pk = id)
    return render(request,'detail.html',{'blogInformation' : blogInformation})
