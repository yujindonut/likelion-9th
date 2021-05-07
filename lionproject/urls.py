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
from django.urls import path, include
from staticBlog.views import homePage
from mediaformBlog.views import home
from django.conf import settings
from django.conf.urls.static import static

#blog안의 views.py안의 모든 함수를 가져온다는 것

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',homePage,name="homePage"),
    path('homemedia/',home,name="home"),
    path('staticBlog/', include('staticBlog.urls')),
    path('mediaformBlog/', include('mediaformBlog.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #이거를 통해 미디어를 url로 설정할 수 있다

