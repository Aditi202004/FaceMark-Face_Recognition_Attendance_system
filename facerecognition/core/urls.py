from django.urls import path,reverse
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('attendance_predict/',attendance_predict,name="attendance"),
    path('class_room/',class_room,name="class_room"),
    path('stu_image/',students_enroll,name="stu_image"),
    path('',home,name="home"),
    path('csv/',csv,name="csv"),
    path('csv/download/<str:class_name>/<str:date>',csv_download,name="download"),
   
    
    # path('home/',video_cam,name="video"),
    # path('video_cam/',attendance_predict_video_cam,name="video_cam")

] 

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)