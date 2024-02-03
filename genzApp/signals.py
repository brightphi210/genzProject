
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse
from .models import *


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        if instance.is_user == True:
            UserProfile.objects.create(user=instance)
            print('Profile created successfully')


        elif instance.is_author == True:
            AuthorsProfile.objects.create(author=instance)

        elif instance.is_admin == True:
            AdminProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def update_profile(sender, instance, created, **kwargs):
    
    try:
        if created == False:
            if instance.is_user == True:
                instance.Userprofile.save()
                print('Profile updated successfully')

            if instance.is_author == True:
                instance.AuthorsProfile.save()
                print('Profile updated successfully')

            if instance.is_admin == True:
                instance.AdminProfile.save()
                print('Profile updated successfully')

    except:
        instance.userprofile = None


@receiver(post_save, sender=User)
def send_email_confirmation(sender, instance, created, **kwargs):
    if created:
        subject = 'Confirm your email'
        confirmation_url = reverse('confirm_email', args=[instance.id])
        message = f'Click the link to confirm your email: {settings.BASE_URL}{confirmation_url}'
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [instance.email]   
        
        send_mail(subject, message, from_email, recipient_list)

