from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.http import HttpResponse

def mail(request):
    if request.method =='POST':
        name= request.POST.get('name')
        email= request.POST.get('email')
        subject= request.POST.get('subject')
        body= request.POST.get('body')

        data={
            'name':name,
            'email':email,
            'subject':subject,
            'body':body,
        }
        #print(data)
        body= '''
        New Mail :{}
        From : {}'''.format(data['body'],data['email'])
        send_mail(data['subject'],body,'',['dbfla87723@gmail.com'])
        return HttpResponse('Thank you for sending the mail.')
    return render(request,'mail.html')
