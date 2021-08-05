from django.shortcuts import render, redirect
from django.core.mail import send_mail


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
        send_mail(data['subject'],body,'',['eunmoong@gmail.com'])
    return render(request,'mail.html')
'''
def sendmail(request):
    send_mail('Hello Dear',
              'Hi there, lalaala',
              'gpg5005@naver.com',
              ['eunmoong@gmail.com'],
              fail_silently=False)

    return redirect('/')
'''