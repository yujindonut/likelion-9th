from django.shortcuts import render
from .models import BlogData
# Create your views here.
def news(request):
    posts=BlogData.objects.all().order_by('-id')
    return render(request,"news.html",{'newsContents':posts})
