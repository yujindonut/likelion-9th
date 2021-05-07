from django.shortcuts import render, redirect, get_object_or_404 
from django.utils import timezone
from .models import mediaformBlog
from .forms import BlogForm

def home(request): 
    blogInfo = mediaformBlog.objects.all() 
    return render(request, 'homeMedia.html', {'blogInfo' : blogInfo})

def detailMedia(request,id):
    blogInformation = get_object_or_404(mediaformBlog, pk = id)
    return render(request, 'detailMedia.html', {'blogInformation' : blogInformation})

def newMedia(request):
    Myform = BlogForm()
    return render(request,'newMedia.html', {'form': Myform})

def createMedia(request):
    form = BlogForm(request.POST, request.FILES)
    if form.is_valid():
        newBlog = form.save(commit=False) #날짜까지 저장해줘야하니까 아직 다 저장못했어~
        newBlog.date = timezone.now()#얘도 추가 저장
        newBlog.save()
        return redirect('detailMedia', newBlog.id)
        #유효성검사에 성공해서 글을 저장했을 때
    return redirect('home')
    #유효성 검사에 실패했을 때는 home으로 가게

def editMedia(request, id):
    editBlog = mediaformBlog.objects.get(id = id)
    return render(request,'editMedia.html',{'blog':editBlog})
    
def updateMedia(request, id):
    updateBlog = mediaformBlog.objects.get(id = id)
    updateBlog.subject = request.POST['titleName']
    updateBlog.drafter = request.POST['writerName']
    updateBlog.textBody = request.POST['bodyContent']
    updateBlog.date = timezone.now() 
    updateBlog.save()
    return redirect('detailMedia', updateBlog.id)

def deleteMedia(request, id):
    deleteBlog = mediaformBlog.objects.get(id = id)
    deleteBlog.delete()
    return redirect('home')
    