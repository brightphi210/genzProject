# Generated by Django 4.2.5 on 2023-12-10 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genzApp', '0009_rename_image_user_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
