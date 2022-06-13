"""lionproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blog.views import * 
#blog안의 views.py안의 모든 함수를 가져온다는 것
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',FirstPage,name="FirstPage"),
    # 오류가 났던 부분 ,를 붙이지 않아서 syntaxError가 계속해서 났다
    path('<str:id>',detail,name="detail"),
] 
#정적 이미지파일 
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)