# Generated by Django 3.1.2 on 2020-12-24 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumni_app', '0019_auto_20201224_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='placement_companies_model',
            name='month',
            field=models.CharField(blank=True, choices=[('january', 'January'), ('february', 'February'), ('march', 'March'), ('april', 'April'), ('may', 'May'), ('june', 'June'), ('july', 'July'), ('august', 'August'), ('september', 'September'), ('october', 'October'), ('november', 'November'), ('december', 'December')], default='august', max_length=9),
        ),
    ]