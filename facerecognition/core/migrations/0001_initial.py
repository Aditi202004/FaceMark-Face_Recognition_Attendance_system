# Generated by Django 4.2.6 on 2023-11-09 16:08

import core.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_name', models.CharField(max_length=100)),
                ('prof_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Date_Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.classes')),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sname', models.CharField(max_length=1000)),
                ('rollNumber', models.CharField(max_length=100, unique=True)),
                ('cid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.classes')),
            ],
        ),
        migrations.CreateModel(
            name='StudentImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rollNumber', models.CharField(max_length=1000)),
                ('image', models.ImageField(upload_to=core.models.file_path)),
                ('sid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.students')),
            ],
        ),
        migrations.CreateModel(
            name='Date_Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to=core.models.file_path_date)),
                ('date', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.date_course')),
            ],
        ),
        migrations.CreateModel(
            name='Attendance_Date',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attendance_mark', models.CharField(choices=[('present', '1'), ('absent', '0')], default='absent', max_length=20)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.classes')),
                ('date', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.date_course')),
                ('sid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.students')),
            ],
        ),
    ]
