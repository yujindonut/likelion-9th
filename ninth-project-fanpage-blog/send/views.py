from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.mail import send_mail,EmailMessage
def base(request):
    return render(request, 'base.html')
def sendmail(request):

    if request.method == 'POST' :
        name = request.POST.get('full-name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # data = {
        #     'name':name,
        #     'email':email,
        #     'subject':subject,
        #     'message':message
        # }
        # message = '''
        # New message: {}

        # From: {}
        # '''.format(data['message'],data['email'])
        mail = EmailMessage(subject, message, to=[email])
        mail.send()
        # send_mail(data['subject'], message,'', ['email'])
        # print(data)
    return render(request, 'index.html')
    # 보냈다는 것을 알기 위해 맨 처음 화면으로 가게끔 