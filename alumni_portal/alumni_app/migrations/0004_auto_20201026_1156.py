# Generated by Django 3.1.2 on 2020-10-26 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumni_app', '0003_auto_20201026_1153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='file',
            field=models.FileField(default='', upload_to='notice'),
        ),
    ]
