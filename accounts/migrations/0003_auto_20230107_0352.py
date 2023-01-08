# Generated by Django 3.2.16 on 2023-01-07 03:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('advisors', '0001_initial'),
        ('accounts', '0002_auto_20230102_1313'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='advisor',
            field=models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='advisors.advisor'),
        ),
        migrations.AddField(
            model_name='user',
            name='is_advisor',
            field=models.BooleanField(default=False),
        ),
    ]