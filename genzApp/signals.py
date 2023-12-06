from django.db.models.signals import post_save
from django.dispatch import receiver

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


# @receiver(post_save, sender=Authors)
# def create_profile(sender, instance, created, **kwargs):
#     if created:
#         AuthorsProfile.objects.create(author=instance)
#         print('Profile created successfully')

# @receiver(post_save, sender=Authors)
# def update_profile(sender, instance, created, **kwargs):
    
#     try:
#         if created == False:
#             instance.AuthorProfile.save()
#             print('Profile updated successfully')

#     except:
#         instance.authorprofile = None
