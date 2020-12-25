# Generated by Django 3.1.2 on 2020-12-24 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumni_app', '0017_auto_20201224_1255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bba_students_model',
            name='rollno',
            field=models.PositiveIntegerField(blank=True, unique=True),
        ),
        migrations.AlterField(
            model_name='bca_students_model',
            name='rollno',
            field=models.PositiveIntegerField(blank=True, unique=True),
        ),
        migrations.AlterField(
            model_name='bcom_students_model',
            name='rollno',
            field=models.PositiveIntegerField(blank=True, unique=True),
        ),
        migrations.AlterField(
            model_name='bed_students_model',
            name='rollno',
            field=models.PositiveIntegerField(blank=True, unique=True),
        ),
    ]
