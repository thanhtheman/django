from django.contrib.auth.models import User
from .models import Profile
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete

#the old way is we need to create a User, then create a Profile
# The new way: whenever a user is created, we automatically create the Profile (with some basic information)

#sender = User, instance = user
def create_user(instance, created, **kwargs):
    if created:
        print('a new user is created')
        user = instance
        Profile.objects.create(
            user = user,
            username = user.username,
            name = user.first_name,
            email = user.email)

def delete_user(instance, **kwargs):
    user = instance.user
    print('a profile is deleted')
    user.delete()


post_save.connect(create_user, sender=User)
post_delete.connect(delete_user, sender=Profile)
