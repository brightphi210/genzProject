# Generated by Django 4.2.5 on 2024-01-24 21:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('genzApp', '0023_magazine'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='magazine',
            name='description',
        ),
        migrations.RemoveField(
            model_name='magazine',
            name='pdf_file',
        ),
        migrations.RemoveField(
            model_name='magazine',
            name='title',
        ),
    ]
