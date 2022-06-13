
from django.contrib import admin
from django.urls import path,include
from community.views import index
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index,name="index"),
    path('admin/', admin.site.urls),
    path('community/',include('community.urls')),
    path('user/',include('user.urls')),
    path('accounts/',include('allauth.urls')),
    path('mail/',include('mail.urls')),
    path('message/',include('message.urls')),
    path('crawling/',include('crawling.urls')),

    #미정
    path('vaccine/',include('vaccine.urls')),
    path('address/',include('address.urls')),
    
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
