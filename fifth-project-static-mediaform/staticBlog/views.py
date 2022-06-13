from django.shortcuts import render, redirect, get_object_or_404 
from django.utils import timezone
from .models import staticBlog #데이터베이스에서 staticBlog에 대한 정보를 다 가져온다

def homePage(request):
    blogInfo = staticBlog.objects.all()
    return render(request, 'home.html', {'blogInfo' : blogInfo})

#데이터베이스에 필요한 것 request옆에 써줌
def detail(request,id):
    blogInformation = get_object_or_404(staticBlog, pk = id)
    return render(request, 'detail.html', {'blogInformation' : blogInformation})

def new(request):
    return render(request,'new.html')

def create(request):
    newBlog = staticBlog()
    newBlog.subject = request.POST['titleName']
    newBlog.drafter = request.POST['writerName']
    newBlog.textBody = request.POST['bodyContent']
    newBlog.date = timezone.now() 
    newBlog.save()
    return redirect('detail', newBlog.id)

def edit(request, id):
    editBlog = staticBlog.objects.get(id = id)
    return render(request,'edit.html',{'blog':editBlog})

def update(request, id):
    updateBlog = staticBlog.objects.get(id = id)
    updateBlog.subject = request.POST['titleName']
    updateBlog.drafter = request.POST['writerName']
    updateBlog.textBody = request.POST['bodyContent']
    updateBlog.date = timezone.now() 
    updateBlog.save() 
    return redirect('detail', updateBlog.id)

def delete(request, id):
    deleteBlog = staticBlog.objects.get(id = id)
    deleteBlog.delete()
    return redirect('homePage')
    