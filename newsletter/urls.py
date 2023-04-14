from django.urls import path
from .views import Subscribe, mail_letter

urlpatterns = [
    path('subscribe', Subscribe , name='subscribe'),
    path('send_notificatioons', mail_letter , name='send-notificatioons'),
   
]