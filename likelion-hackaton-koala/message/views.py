
from django.shortcuts import render, redirect, get_object_or_404
from .models import Message
from .forms import *
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.db.models import Q
from django.contrib.auth.models import User
# Create your views here.

def messageBox(request):
    return render(request,"messageBox.html")

def messageReception(request):#쪽지 수신함
    message=Message.objects.filter( to = request.user).filter( ~Q( writer = request.user)).order_by('-id')
    return render(request,"reception.html",{'message':message})

def sendMessage(request):#쪽지 발신함
    message=Message.objects.filter( writer = request.user ).filter(~Q(to = request.user)).order_by('-id')
    return render(request,"sendMessage.html",{'message':message})

def sendToMe(request):#내게쓴쪽지
    message=Message.objects.filter( to = request.user , writer  =   request.user ).order_by('-id')
    return render(request,"sendToMe.html",{'message':message})

def detailMessage(request, messageId): 
    message = get_object_or_404(Message, pk = messageId) 
    return render(request, 'detailMessage.html', {'message':message})

def newMessage(request):
    if request.method == 'POST':
        #users=AbstractUser.objects.all()
        #userModel=get_user_model()
        #users=userModel.objects.all()
        
        
        form = MessageForm(request.POST, request.FILES)
        if form.is_valid():
            message = form.save(commit=False)
            message.writer = request.user
            message.pub_date = timezone.now() 
            message.save()
            return redirect("detailMessage",message.id)
    else:
        form = MessageForm()
        users =get_user_model().objects.all().order_by('-username')
        print(users)
        return render(request, 'newMessage.html', {'form':form,'users':users})


def newMessageToMe(request):#내게 쪽지 쓰기
    
    if request.method == 'POST':
        form =MessageToMeForm(request.POST, request.FILES)
        if form.is_valid():
            message = form.save(commit=False)
            message.to = request.user
            message.writer = request.user
            message.pub_date = timezone.now() 
            message.save()
            return redirect("detailMessage",message.id)
    else:
        form = MessageForm()
        return render(request, 'newMessageToMe.html', {'form':form})

def deleteMessage(request,messageId):
   deletePost = get_object_or_404(Message,pk=messageId)
   # handle django 1.4 pickling bug
   #print(deletePost+"1.삭제")
   #print(deletePost.writer+"2.삭제")
   #print(deletePost.CustomUser)
   if str(deletePost.writer) == str(deletePost.to)  :  #내게 쓴 메세지 삭제
        deletePost.delete() #삭제해주는 메소드
        return redirect('sendToMe')
   elif   deletePost.writer != request.user and deletePost.to == request.user: #받은 메세지 삭제
        deletePost.delete() #삭제해주는 메소드
        
        return redirect('messageReception')
   else:#보낸 메세지 삭제
        deletePost.delete() #삭제해주는 메소드
        return redirect('sendMessage')