from django.shortcuts import render, redirect, get_object_or_404 #알 수 없는 페이지를 가져오라고 했을때 404Error를 처리한다.
from .models import Blog #데이터베이스에서 Blog에 대한 정보를 다가져온다
# Create your views here.
from django.utils import timezone
#Blog클래스 안의 date변수를 사용하기 위해서는 현재시각을 알아야한다

#함수를 만들면 urls.py에 path를 작성

#CRUD read : home , detail 기능
def homePage(request): #home
    blogInfo = Blog.objects.all() #blogs
    return render(request, 'home.html', {'blogInfo' : blogInfo})

#데이터베이스에 요청하는 것이 있으면 request옆에 뭘 요청하는지 써준다
def detail(request,id):
    blogInformation = get_object_or_404(Blog, pk = id)
    return render(request, 'detail.html', {'blogInformation' : blogInformation})

#CRUD create : new, create 기능 
def new(request):
    return render(request,'new.html')
    #return render : 새로운 html을 만들어서 request를 보낸다

#데이터베이스에 저장
def create(request):
    #new_blog라는 객체를 만들어서 request의 post방식으로 받은 것을 저장한다.
    newBlog = Blog()
    newBlog.subject = request.POST['titleName']
    newBlog.drafter = request.POST['writerName']
    newBlog.textBody = request.POST['bodyContent']
    newBlog.date = timezone.now() #현재시각을 알려준다
    newBlog.save()
    #어떤 화면으로 이동을 할 것인지?  
    # 새로운 html로 보내는 것이 아니라 원래 있던 html에 보내는 것 : redirect
    return redirect('detail', newBlog.id)

#CRUD Upadate: edit, update
#update는 create와 유사하지만 수정할 데이터의 id값을 받아와야하는 것에서 차이가 있음
def edit(request, id):
    editBlog = Blog.objects.get(id = id)
    return render(request,'edit.html',{'blog':editBlog})

def update(request, id):
    updateBlog = Blog.objects.get(id = id)
    #수정해야될 id를 가져와서 update한 정보로 기존의 데이터 정보를 덮어준다
    updateBlog.name = request.POST['titleName']
    updateBlog.drafter = request.POST['writerName']
    updateBlog.textBody = request.POST['bodyContent']
    updateBlog.date = timezone.now() #현재시각을 알려준다
    updateBlog.save() #저장을 꼭 해줘야야지 데이터베이스에 저장이된다
    return redirect('detail', updateBlog.id)

#CRUD delete
def delete(request, id):
    deleteBlog = Blog.objects.get(id = id)
    deleteBlog.delete()
    return redirect('homePage')
    