from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls')),
    path('shopkeeper/', include('shopkeeper.urls')),
    path('basket/', include('basket.urls')),
     path('newsletter/', include('newsletter.urls')),
    path('customers/', include('django.contrib.auth.urls')),
    path('customers/', include('customers.urls')),
    
   
]+ static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT )
