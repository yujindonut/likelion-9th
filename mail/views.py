from django.shortcuts import render, redirect
from django.core.mail import send_mail


def mail(request):
    return render(request,'mail.html')

def sendmail(request):
    send_mail('Hello Dear',
              'Hi there, lalaala',
              'whitejand@naver.com',
              ['eunmoong@gmail.com'],
              fail_silently=False)

    return redirect('/')
