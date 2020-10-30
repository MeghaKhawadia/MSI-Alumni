# Generated by Django 3.1.2 on 2020-10-30 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumni_app', '0007_auto_20201029_1941'),
    ]

    operations = [
        migrations.CreateModel(
            name='slideshow_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=25)),
                ('description', models.CharField(blank=True, max_length=250)),
                ('photo', models.ImageField(blank=True, default='', upload_to='slideshow')),
            ],
        ),
    ]