from django.contrib import admin

# Register your models here.
from .models import Image,Student

admin.site.register(Image)
admin.site.register(Student)