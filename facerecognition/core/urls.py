from django.urls import path
from .views import home,image,StudentData

urlpatterns = [
    path('home/',home,name="home"),
    path('',image,name="image"),
    path('student/',StudentData, name="student")
]