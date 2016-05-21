from django.db.models.signals import post_save
from django.dispatch import receiver

from videos.models import Video, Rating, Analytic


@receiver(post_save, sender=Video)
def create_analytics(sender, instance, created, **kwargs):
    if created:
        Analytic.objects.create(video=instance)


@receiver(post_save, sender=Video)
def create_rating(sender, instance, created, **kwargs):
    if created:
        Rating.objects.create(video=instance)