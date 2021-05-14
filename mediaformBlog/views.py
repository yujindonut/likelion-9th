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

#new, create함수 하나로 합치기
#http 메소드 중 GET과 POST
#GET은 파라미터 포함해서 보내고, POST는 파라미터 안보이게
#긴글의 내용을 저장, 보이면 안되는 정보들은 POST
def newMedia(request):
    if request.method == 'POST': #글을 작성한 후 저장 버튼을 눌렀을 때 = 파라미터로 받은게 있으면?
        blogForm = BlogForm(request.POST, request.FILES)
        if blogForm.is_valid():
            myblog = blogForm.save(commit = False)#날짜까지 저장해줘야하니까 아직 저장할 것이 남았다
            myblog.date = timezone.now() #날짜 생성
            myblog.save()
            return redirect('detailMedia', myblog.id)
            #유효성검사에 성공해서 글을 저장했을 때
        return redirect('home')
        #유효성 검사에 실패했을 때는 home으로 가게
    else:
        blogForm = BlogForm() #글을 입력받기 위한 빈 form을 불러온다
        return render(request,'newMedia.html', {'form': blogForm}) 

#edit과 update 함수 하나로 합치기
def editMedia(request, id):
    update_blog = get_object_or_404(mediaformBlog,pk=id)
    if request.method == 'GET': 
        blogForm = BlogForm(instance = update_blog)
        return render(request,'editMedia.html', {'form': blogForm}) 
    else: #update #글을 수정하고 수정버튼을 눌렀을 때
        blogForm = BlogForm(request.POST, request.FILES, instance = update_blog)
        #현재 post에 가져온 정보를 form에 담음
        if blogForm.is_valid():
            update_blog = blogForm.save(commit = False)
            update_blog.date = timezone.now()
            update_blog.save()
            return redirect('/mediaformBlog/detail/' + str(id))
            # return redirect('detailMedia', update_blog.id)
        return redirect('home')

def deleteMedia(request, id):
    deleteBlog = mediaformBlog.objects.get(id = id)
    deleteBlog.delete()
    return redirect('home')
    