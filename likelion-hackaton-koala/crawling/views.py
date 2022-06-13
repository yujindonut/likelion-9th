from django.shortcuts import render
from .models import BlogData
from django.core.paginator import Paginator

# Create your views here.
def news(request):
    news = BlogData.objects.all().order_by('-id')
    paginator = Paginator(news, 10)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, "news.html", {'posts': posts})
