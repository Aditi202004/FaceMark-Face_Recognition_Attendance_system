from django.shortcuts import render
from django.contrib import messages
from .models import Image,Student,Attendance
import cv2
from mtcnn.mtcnn import MTCNN
from keras_facenet import FaceNet
import numpy as np
import joblib
# from model import model
detector = MTCNN()
model = joblib.load("model_svc")



# Create your views here.
def home(request):
    return render(request,"input.html")

def image(request):
    present_list = []
    data = {
        "present_list": present_list
    }
    
    if request.method == "POST":
        image = Image()
        # print(request.post)
        print(len(request.FILES))
        if len(request.FILES) != 0:
            print(request.FILES['image'])
            image.image = request.FILES['image']
            data = {
                "message": "Hello"
            }
        
        image.save()
        print(image.image)
        path = str(image.image)
        print(path)
        img = cv2.imread(path)
        img_rgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        output = detector.detect_faces(img_rgb)
        faces = []
        for dect in output:
            x,y,w,h = dect['box']
            face = img_rgb[y:y+h,x:x+w]
            faces.append(face)
        embedder = FaceNet()
        em_list =[]
        for face in faces:
            face_reshape = np.expand_dims(face, axis=0)
            embedding = embedder.embeddings(face_reshape)
            em_list.append(embedding)
        em_list_pro = []
        for i in em_list:
            em_list_pro.append(i[0])

        messages.success(request,"Product Added Successfully")
        print("Hello")
        present_list = model.predict(em_list_pro)
        # print(present_list)
        # print(present_list[0][0])

    data = {
        "present_list": present_list
    }
    

    return render(request,'input.html',data)
    
def StudentData(request):
    if request.method == "POST":
        info = request.POST
        student = Student()
        student.name = info['name']
        student.rollNumber = info['rollnumber']
        student.save()
        print(Student.objects.all())
        print(info)
    return render(request,'student.html')