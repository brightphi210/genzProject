# Generated by Django 4.1.1 on 2024-02-03 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genzApp', '0029_remove_passwordreset_new_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='code',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        migrations.DeleteModel(
            name='PasswordReset',
        ),
    ]
