from django.shortcuts import render
# Create your views here.
def vaccine(request):
    return render(request,"vaccine.html")
