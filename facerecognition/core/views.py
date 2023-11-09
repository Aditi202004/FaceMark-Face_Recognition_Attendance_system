from django.shortcuts import render
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import *
import os
import cv2
from .get_embeddings import get_embeddings
from .check import get_list
from django.conf import settings

# Create your views here.
def home(request):
    return render(request, "input.html")

def class_room(request):
    if request.method == "POST":
        info = request.POST
        print(info)
        class_name = info['class']
        prof_name = info['prof_name']
        class_room = Classes()
        class_room.c_name = class_name
        class_room.prof_name = prof_name
        class_room.save()
        print(Classes.objects.all())
        print(info)
        return render(request,'input.html')
    return render(request,'class.html')


def students_enroll(request):
    class_list = []
    for i in Classes.objects.all():
        class_list.append(i.c_name)
    data = {
        "class_list": class_list
    }
    print(class_list)
    if request.method == "POST":
        info = request.POST
        print(info)
        c_name = info['class_name']
        sname = info['sname']
        rollNumber = info['rollNumber']
        print('hi hello')
        bool = Students.objects.filter(rollNumber=rollNumber).exists()
        print('hi')
        print(bool)
        print('hello')
        if bool!= True:
            student = Students()
            class_room = Classes.objects.get(c_name = c_name)
            print(class_room)
            student.cid = class_room
            student.sname = sname
            student.rollNumber = rollNumber
            student.save()
        else :
            student = Students.objects.get(rollNumber = rollNumber)
            print(student)
        print(Students.objects.all())
        images = request.FILES.getlist('image')

        for img in images:
            stu_image = StudentImages()
            stu_image.sid = student
            stu_image.rollNumber = student.rollNumber
            stu_image.image = SimpleUploadedFile(img.name, img.read())  # Create a SimpleUploadedFile from the uploaded file
            stu_image.save()
            print(StudentImages.objects.all())
        print("directory created")
        # directory = os.path.join('../static/images/',rollNumber)
        # directory = '../static/images'
        directory = os.path.join(settings.BASE_DIR, 'static','images',rollNumber)
        # print(directory)
        # list_dir = get_list(directory)
        for filename in os.listdir(directory):
            f = os.path.join(directory, filename)
            print(f)
            img = cv2.imread(f)
            print("hi image")
            get_embeddings(c_name, img, rollNumber)

            
    return render(request,'studentimages.html',data)

    