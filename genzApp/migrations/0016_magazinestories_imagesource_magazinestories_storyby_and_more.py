# Generated by Django 4.2.5 on 2024-01-01 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genzApp', '0015_alter_user_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='magazinestories',
            name='imageSource',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='magazinestories',
            name='storyBy',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='stories',
            name='imageSource',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='stories',
            name='storyBy',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_pic',
            field=models.ImageField(blank=True, default='profile_pics/default.png', null=True, upload_to='profile_pics/'),
        ),
    ]
