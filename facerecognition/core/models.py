from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
import os


# options
ATTENDANCE_MARK = (
    ("present","1"),
    ("absent","0")
)
 

# Create your models here.


class Classes(models.Model):
    c_name = models.CharField(max_length=100)
    prof_name = models.CharField(max_length=100)

class Students(models.Model):
    sname = models.CharField(max_length=1000)
    rollNumber = models.CharField(max_length=100,unique=True)
    # image = models.ImageField(upload_to=f'static/images/students/{rollNumber}')
    cid = models.ForeignKey(Classes,on_delete=models.CASCADE)

def file_path(instance,filename):
    print(os.path.join('static/images/',instance.rollNumber,filename))
    return os.path.join('static/images/',instance.rollNumber,filename)

class StudentImages(models.Model):
    sid = models.ForeignKey(Students,on_delete=models.CASCADE)
    rollNumber = models.CharField(max_length=1000)
    image = models.ImageField(upload_to=file_path)

# class Date(models.Model):
#     date = models.DateField(auto_now=True)
#     course = models.ForeignKey(Classes,on_delete=models.CASCADE)



# class Attendance(models.Model):
#     date  = models.ForeignKey(Date,on_delete=models.CASCADE)
#     c_name = models.ForeignKey(Classes,on_delete=models.CASCADE)
#     sid = models.ForeignKey(Students, on_delete=models.CASCADE)
#     attendance_mark = models.CharField(
#         max_length=20,
#         choices=ATTENDANCE_MARK,
#         default='absent'
#     )

class Date_Course(models.Model):
    date = models.DateField()
    course_id = models.ForeignKey(Classes,on_delete=models.CASCADE)

def file_path_date(instance,filename):
    return os.path.join('static/images/',str(instance.date.date),filename)

class Date_Image(models.Model):
    date = models.ForeignKey(Date_Course,on_delete=models.CASCADE)
    images = models.ImageField(upload_to=file_path_date)

class Attendance_Date(models.Model):
    date  = models.ForeignKey(Date_Course,on_delete=models.CASCADE)
    course = models.ForeignKey(Classes,on_delete=models.CASCADE)
    sid = models.ForeignKey(Students, on_delete=models.CASCADE)
    attendance_mark = models.CharField(
        max_length=20,
        choices=ATTENDANCE_MARK,
        default='absent'
    )

class Image(models.Model):
    image = models.ImageField(upload_to='media/static/images/video_cam')


