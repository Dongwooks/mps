from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from main.views import home, section1,tag_section1, tag_section2

urlpatterns = [
    path('bathon/', include('baton.urls')),

    path('admin/', admin.site.urls),
    path('main/', include('main.urls')),
    
    url('main/tag_section1/', tag_section1),
    url('main/tag_section2/', tag_section2),
    path('', home),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
