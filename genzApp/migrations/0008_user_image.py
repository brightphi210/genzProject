# Generated by Django 4.2.5 on 2023-12-10 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genzApp', '0007_newsletter_subscriptionplan'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, default='default.png', null=True, upload_to='profile_pics/'),
        ),
    ]