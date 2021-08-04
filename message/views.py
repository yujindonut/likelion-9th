from django.shortcuts import render, redirect, get_object_or_404
from .models import Message
from .forms import MessageForm
from django.utils import timezone
# Create your views here.

def messageBox(request):
    return render(request,"messageBox.html")

def messageReception(request):
    message=Message.objects.filter( to = request.user)
    return render(request,"reception.html",{'message':message})

def sendMessage(request):
    message=Message.objects.filter( writer = request.user)
    return render(request,"sendMessage.html",{'message':message})


def detailMessage(request, messageId): 
    message = get_object_or_404(Message, pk = messageId) 
    return render(request, 'detailMessage.html', {'message':message})

def newMessage(request):
    if request.method == 'POST':
        form = MessageForm(request.POST, request.FILES)
        if form.is_valid():
            message = form.save(commit=False)
            message.writer = request.user
            message.pub_date = timezone.now() 
            message.save()
            return redirect("detailMessage",message.id)
    else:
        form = MessageForm()
        return render(request, 'newMessage.html', {'form':form})
'''
def delete(request,messageId):
   deletePost = get_object_or_404(Message,pk=messageId)
   deletePost.delete() #삭제해주는 메소드
   return redirect('home')'''