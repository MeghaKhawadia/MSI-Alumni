# Generated by Django 3.1.2 on 2021-06-12 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumni_app', '0023_auto_20210108_1833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bed_students_model',
            name='email',
            field=models.EmailField(blank=True, default='', max_length=40),
        ),
    ]
