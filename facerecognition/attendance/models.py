from django.db import models
from django.contrib.auth.models import User


# options
ATTENDANCE_MARK = (
    ("present","1"),
    ("absent","0")
)
 

# Create your models here.


class Class(models.Model):
    c_name = models.CharField(max_length=100)
    prof_name = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.c_name

class Students(models.Model):
    sid = models.AutoField(primary_key=True)
    sname = models.CharField(max_length=1000,blank = None)
    rollNumber = models.CharField(max_length=100,blank=None)
    image = models.ImageField(upload_to=f'static/images/students/{rollNumber}')
    cid = models.ForeignKey(Class,on_delete=models.CASCADE)
    def __int__(self) ->int:
        return self.sid

class Date(models.Model):
    date = models.DateField(blank=False,auto_now=True)


class Attendance(models.Model):
    date  = models.ForeignKey(Date,on_delete=models.CASCADE)
    c_name = models.ForeignKey(Class,on_delete=models.CASCADE)
    sid = models.ForeignKey(Students, on_delete=models.CASCADE)
    attendance_mark = models.CharField(
        max_length=20,
        choices=ATTENDANCE_MARK,
        default='absent'
    )
    def __date__(self) ->date:
        return self.date


