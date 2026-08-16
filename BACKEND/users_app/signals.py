from django.db.models.signals import post_save
from django.dispatch import receiver

from ranks_app.models import Rank
from .models import PlayerProfile, User



@receiver(post_save, sender=User)
def create_player_profile(sender, instance, created, **kwargs):
    if created:
        first_rank = Rank.objects.order_by('order').first()
        PlayerProfile.objects.create(
            user=instance,
            current_rank=first_rank
        )