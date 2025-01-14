# Generated by Django 3.1.2 on 2020-10-29 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumni_app', '0006_slideshow_model'),
    ]

    operations = [
        migrations.CreateModel(
            name='bba_students_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(blank=True, max_length=25)),
                ('lname', models.CharField(blank=True, max_length=25)),
                ('rollno', models.PositiveIntegerField(blank=True, unique=True)),
                ('file', models.FileField(blank=True, default='', upload_to='alumni')),
            ],
        ),
        migrations.CreateModel(
            name='bca_students_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(blank=True, max_length=25)),
                ('lname', models.CharField(blank=True, max_length=25)),
                ('rollno', models.PositiveIntegerField(blank=True, unique=True)),
                ('file', models.FileField(blank=True, default='', upload_to='alumni')),
            ],
        ),
        migrations.CreateModel(
            name='bcom_students_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(blank=True, max_length=25)),
                ('lname', models.CharField(blank=True, max_length=25)),
                ('rollno', models.PositiveIntegerField(blank=True, unique=True)),
                ('file', models.FileField(blank=True, default='', upload_to='alumni')),
            ],
        ),
        migrations.CreateModel(
            name='bed_students_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(blank=True, max_length=25)),
                ('lname', models.CharField(blank=True, max_length=25)),
                ('rollno', models.PositiveIntegerField(blank=True, unique=True)),
                ('file', models.FileField(blank=True, default='', upload_to='alumni')),
            ],
        ),
        migrations.DeleteModel(
            name='slideshow_model',
        ),
    ]
