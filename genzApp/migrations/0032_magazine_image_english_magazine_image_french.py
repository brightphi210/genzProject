# Generated by Django 4.1.1 on 2024-02-04 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genzApp', '0031_remove_user_code_passwordreset'),
    ]

    operations = [
        migrations.AddField(
            model_name='magazine',
            name='image_english',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='magazine',
            name='image_french',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]