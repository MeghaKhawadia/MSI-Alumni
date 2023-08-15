# Generated by Django 3.1.2 on 2021-06-14 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumni_app', '0024_auto_20210612_1753'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=25)),
                ('lname', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=35)),
                ('subject', models.TextField(max_length=250)),
            ],
        ),
    ]