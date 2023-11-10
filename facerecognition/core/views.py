from django.shortcuts import render,redirect
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import *
import os
import cv2
from .get_embeddings import get_embeddings
from .check import get_list
from django.conf import settings
from .predict import predict
import pandas as pd
from django.http import FileResponse,HttpResponse
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages


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
    # return render(request,'class.html')
    return render(request,'register.html')


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
            stu_image.image = SimpleUploadedFile(img.name,img.read())
            # Create a SimpleUploadedFile from the uploaded file
            stu_image.save()
            print(StudentImages.objects.all())
        print("directory created")
        # directory = os.path.join('../static/images/',rollNumber)
        # directory = '../static/images'
        directory = os.path.join(settings.BASE_DIR, 'media/static','images',rollNumber)
        # print(directory)
        # list_dir = get_list(directory)
        for filename in os.listdir(directory):
            f = os.path.join(directory, filename)
            print(f)
            img = cv2.imread(f)
            print("hi image")
            get_embeddings(c_name, img, rollNumber) 
            

    # return render(request,'studentimages.html',data)
    return render(request,'newStudent.html',data)

def attendance_predict(request):
    class_list = []
    course = Classes.objects.all()
    for i in course:
        class_list.append(i.c_name)
    data = {
        "class_list":class_list
    }
    print('Hello')
    if request.method == "POST":
        print('post')
        info = request.POST
        date_course = Date_Course()
        print(info['date'])
        date_course.date = info['date']
        course_id = Classes.objects.get(c_name = info['class_name'])
        date_course.course_id = course_id
        date_course.save()
        date_str = str(info['date'])
        directory = os.path.join(settings.BASE_DIR, 'media/static','images',date_str)
        print(directory)
        print('hell')
        print(os.path.exists(directory))
        if os.path.exists(directory) == False:
            print("hello")
            os.mkdir(directory)
        images = request.FILES.getlist('images')
        print(date_course)
        print(images)
        for img in images:
            print(img)
            date_image = Date_Image()
            date_image.date = date_course
            date_image.images = SimpleUploadedFile(img.name, img.read())
            date_image.save()
        
        img_list = []
        for filename in os.listdir(directory):
            f = os.path.join(directory, filename)
            img = cv2.imread(f)
            img_list.append(img)
        print(img_list)
        roll = predict(img_list,info['class_name'])
        print(roll)
        data = {
            'date': info['date'],
            'roll': roll
        }
        course_id = Classes.objects.get(c_name = info['class_name'])
        students = Students.objects.filter(cid = course_id)
        csv_dict = {
            'roll_numbers': [],
            'name': [],
            'attendance_status' : []
        }
        attendance_dict ={}
        for student in students:
              csv_dict['roll_numbers'].append(student.rollNumber)
              csv_dict['name'].append(student.sname)
              print(student.rollNumber[-4:])
              attendance_dict[student.rollNumber[-4:]] = 0

        for i in roll:
            attendance_dict[i] = 1
        for i,student in enumerate(students):
            csv_dict['attendance_status'].append(attendance_dict[csv_dict['roll_numbers'][i][-4:]]) 
        df = pd.DataFrame(csv_dict)
        file = f'{date_str}.csv'
        directory_csv = os.path.join(settings.BASE_DIR,'media/static/csv',course_id.c_name)
        if os.path.exists(directory_csv) == False:
            os.makedirs(directory_csv)
        # Save the dataframe to a CSV file
        directory_csv = directory_csv+'/'+file
        df.to_csv(directory_csv, index=False)


    # return render(request,'attendance.html',data)
    return render(request,'face_recognition.html',data)

# def video_cam(request):
#     return render(request,'home.html')

# def attendance_predict_video_cam(request):
#     class_list = []
#     course = Classes.objects.all()
#     for i in course:
#         class_list.append(i.c_name)
#     data = {
#         "class_list":class_list
#     }
#     print('Hello')
#     if request.method == "POST":
        
#         print('post')
#         info = request.POST
#         print(info)
#         image_data_json = json.loads(request.body.decode('utf-8'))
#         print(image_data_json)
#         image_data = image_data_json['imageData']
#         print(image_data)
#         image_data_model = Image()
#         image_data_model.image = SimpleUploadedFile("webcam_image.png",image_data.read())
#         image_data_model.save()
#         print(image_data)
#         date_course = Date_Course()
#         date_course.date = info['date']
#         course_id = Classes.objects.get(c_name = info['class_name'])
#         date_course.course_id = course_id
#         date_course.save()
#         date_str = str(info['date'])
#         directory = os.path.join(settings.BASE_DIR, 'media/static','images',date_str)
#         print('hell')
#         if os.path.exists(directory) == False:
#             os.mkdir(directory)
#         images = request.FILES.getlist('images')
#         print(images)
#         for img in images:
#             print(img)
#             date_image = Date_Image()
#             date_image.date = date_course
#             date_image.images = SimpleUploadedFile(img.name, img.read())
#             date_image.save()
        
#         img_list = []
#         for filename in os.listdir(directory):
#             f = os.path.join(directory, filename)
#             img = cv2.imread(f)
#             img_list.append(img)
#         print(img_list)
#         roll = predict(img_list,info['class_name'])
#         print(roll)
#         data = {
#             'date': info['date'],
#             'roll': roll
#         }
#         course_id = Classes.objects.get(c_name = info['class_name'])
#         students = Students.objects.filter(cid = course_id)
#         csv_dict = {
#             'roll_numbers': [],
#             'name': [],
#             'attendance_status' : []
#         }
#         attendance_dict ={}
#         for student in students:
#               csv_dict['roll_numbers'].append(student.rollNumber)
#               csv_dict['name'].append(student.sname)
#               print(student.rollNumber[-4:])
#               attendance_dict[student.rollNumber[-4:]] = 0

#         for i in roll:
#             attendance_dict[i] = 1
#         for i,student in enumerate(students):
#             csv_dict['attendance_status'].append(attendance_dict[csv_dict['roll_numbers'][i][-4:]]) 
#         df = pd.DataFrame(csv_dict)
#         file = f'{date_str}.csv'
#         directory_csv = os.path.join(settings.BASE_DIR,'media/static/csv',file)
#         # Save the dataframe to a CSV file
#         df.to_csv(directory_csv, index=False)


#     return render(request,'home.html',data)
def csv(request):
    class_list = []
    class_list = []
    course = Classes.objects.all()
    for i in course:
        class_list.append(i.c_name)
    data = {
        "class_list":class_list
    }
    if request.method == "POST":
        info = request.POST
        date = info['date']
        class_name = info['class_name']
        print(class_name)
        date = str(date)
        return redirect(f'download/{class_name}/{date}')
    return render(request,"download_csv.html",data)

def csv_download(request,class_name,date):
    print(class_name,date)
    file = f'{date}.csv'
    directory = os.path.join(settings.BASE_DIR,'media/static/csv',class_name,file)
    print(directory)
    if os.path.exists(directory):
        file_name = os.path.basename(file)
        response = FileResponse(open(directory, 'rb'))
        response['Content-Disposition'] = f'attachment; filename="{file_name}"'
        print("Hello")
        return response
    return HttpResponse("File not found", status=404)
