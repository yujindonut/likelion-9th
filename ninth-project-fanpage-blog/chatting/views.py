from django.core.mail import message
from django.shortcuts import render, redirect, get_object_or_404 
from .models import Message
from .views import *
from .forms import MessageForm
from django.utils import timezone

def receive_message(request):
    chats = Message.objects.filter( receiver = request.user ) #DB에서 내가 받은 것만 필터링
    return render(request,"chat_received.html", {'chats': chats})

def send_message(request):
    chats=Message.objects.filter( sender = request.user) #내가 보낸 것만 필터링
    return render(request,"chat_send.html",{'chats': chats})

def detail_message(request, id):
    chat =get_object_or_404(Message, pk = id)
    return render(request, 'chat_detail.html', {'chat': chat})

def new_message(request): 
    if request.method == 'POST' : 
        chatform = MessageForm(request.POST, request.FILES)
        if chatform.is_valid():
            chat = chatform.save(commit = False)
            chat.date = timezone.now()
            chat.save()
            return redirect('detail_message', chat.id)
        return redirect('send_message') #실패하면 내가 보낸 메세지함으로 가게
    else: 
        chatform = MessageForm()
        return render(request,'chat_new.html', {'chatform' : chatform})

def edit_message(request,id):
    chat = get_object_or_404(Message, pk = id)
    if request.method == 'POST': 
        chatform = MessageForm(request.POST, request.FILES, instance = chat)
        #현재 post에 가져온 정보를 form에 담는다
        if chatform.is_valid():
            chat = chatform.save(commit = False)
            chat.date = timezone.now()
            chat.save()
            return redirect('detail_message', chat.id)#글이 저장되었으면 detail페이지  
        return redirect('send_message') #가져온정보가 유효하지 않을 때 home으로 가게
    else: #Get방식
        chatform = MessageForm(instance = chat)
        return render(request, 'chat_edit.html', {'chatform' : chatform})
        #수정된 정보를 edit.html에 보내준다.

def delete_message(request,id) :
    delete = Message.objects.get(id = id)
    delete.delete()
    return redirect('receive_message')    