# Generated by Django 3.2.16 on 2023-01-11 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('observers', '0002_auto_20230111_1603'),
        ('students', '0001_initial'),
        ('companies', '0003_auto_20230111_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='followers',
            field=models.ManyToManyField(related_name='following_companies', through='observers.Follow', to='students.Student'),
        ),
    ]
