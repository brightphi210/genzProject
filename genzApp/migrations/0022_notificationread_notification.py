# Generated by Django 4.2.5 on 2024-01-07 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('genzApp', '0021_remove_notificationread_message_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='notificationread',
            name='notification',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='genzApp.notification'),
        ),
    ]