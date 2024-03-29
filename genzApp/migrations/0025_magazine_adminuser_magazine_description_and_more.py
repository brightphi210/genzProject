# Generated by Django 4.2.5 on 2024-01-24 21:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('genzApp', '0024_remove_magazine_description_remove_magazine_pdf_file_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='magazine',
            name='adminUser',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='magazine',
            name='description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='magazine',
            name='pdf_file_english',
            field=models.FileField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='magazine',
            name='pdf_file_french',
            field=models.FileField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='magazine',
            name='title_english',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='magazine',
            name='title_french',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
