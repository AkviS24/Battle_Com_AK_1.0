from django.contrib.auth.models import AbstractUser
from django.db import models

from ranks_app.models import Rank

# Create your models here.

class User(AbstractUser):
    callsign = models.CharField(
        max_length=50,
        unique=True
    )
    discord_id = models.CharField(
        max_length=100,
        unique=True,
        null=True,
        blank=True
    )


class PlayerProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile'
    )
    xp = models.PositiveIntegerField(default=0)
    current_rank = models.ForeignKey(
        Rank,
        on_delete=models.PROTECT,
        related_name='players'
    )