# Generated by Django 4.2.5 on 2023-12-10 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('genzApp', '0008_user_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='image',
            new_name='profile_pic',
        ),
    ]