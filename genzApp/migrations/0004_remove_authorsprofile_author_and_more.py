# Generated by Django 4.2.5 on 2023-12-06 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genzApp', '0003_magazinestories'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='authorsprofile',
            name='author',
        ),
        migrations.RemoveField(
            model_name='magazinestories',
            name='author',
        ),
        migrations.RemoveField(
            model_name='magazinestories',
            name='category',
        ),
        migrations.RemoveField(
            model_name='news',
            name='author',
        ),
        migrations.RemoveField(
            model_name='news',
            name='category',
        ),
        migrations.DeleteModel(
            name='NewsLetter',
        ),
        migrations.RemoveField(
            model_name='stories',
            name='author',
        ),
        migrations.RemoveField(
            model_name='stories',
            name='category',
        ),
        migrations.RemoveField(
            model_name='subscriptionplan',
            name='user',
        ),
        migrations.AddField(
            model_name='user',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='is_author',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='is_user',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='Authors',
        ),
        migrations.DeleteModel(
            name='AuthorsProfile',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='MagazineStories',
        ),
        migrations.DeleteModel(
            name='News',
        ),
        migrations.DeleteModel(
            name='Stories',
        ),
        migrations.DeleteModel(
            name='SubscriptionPlan',
        ),
    ]
