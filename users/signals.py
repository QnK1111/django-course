from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Profile
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def profileUpdated(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user = user,
            username = user.username,
            email = user.email,
            name = user.first_name,
        )

@receiver(post_delete, sender=Profile) 
def profileDeleted(sender, instance, **kwargs):
    instance.user.delete()

@receiver(post_save, sender=Profile)    
def updateUser(sender, instance, created, **kwargs):
    profile = instance
    user = profile.user
    
    if created == False:
        user.first_name = profile.name
        user.username = profile.username
        user.email = profile.email
        user.save()