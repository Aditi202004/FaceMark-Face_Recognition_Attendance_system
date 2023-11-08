from django.db import models
import os
import datetime

# Create your models here.
def filepath(request, filename):
    return os.path.join('static/images',filename)

class Image(models.Model):
    image = models.ImageField(upload_to=filepath,null=True,blank=True)

class Student(models.Model):
    rollNumber = models.DecimalField(max_digits=30,decimal_places=0)
    name = models.CharField(max_length=200)
    
class Attendance(models.Model):
    student_id = models.ForeignKey("Student",on_delete=models.DO_NOTHING)
    present_count = models.DecimalField(max_digits=4,decimal_places=0,default=0)
    absent_count = models.DecimalField(max_digits=4,decimal_places=0,default=0)
    today_date = {
        f"{models.DateField(default=datetime.date.today())}": models.BooleanField(default=False)
    }
    previous_date = {
        f"{models.DateField()}": models.BooleanField(default=False)
    }
    total_presentense_dates = previous_date.update(today_date)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)    
    objects = models.Manager()



