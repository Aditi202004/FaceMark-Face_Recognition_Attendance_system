from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',home,name="home"),
    path('class_room/',class_room,name="class_room"),
    path('stu_image/',students_enroll,name="stu_image")

] 

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)