from django.db.models.signals import post_save
from user.models import UserAcc, UserAccProfile
from django.dispatch import receiver


@receiver(post_save, sender=UserAcc)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserAccProfile.objects.create(user=instance)


@receiver(post_save, sender=UserAcc)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
