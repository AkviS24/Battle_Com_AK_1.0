from django.conf import settings
from django.db import models

# Create your models here.

class Rank(models.Model):
    name = models.CharField(max_length=50, unique=True)
    abbreviation = models.CharField(max_length=10, unique=True)
    min_xp = models.PositiveIntegerField()
    category = models.CharField(max_length=30)
    order = models.PositiveIntegerField(unique=True)
    requires_approval = models.BooleanField(default=False)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f'{self.name} ({self.abbreviation})'


class Promotion(models.Model):
    player = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='promotions'
    )
    from_rank = models.ForeignKey(
        Rank,
        on_delete=models.PROTECT,
        related_name='promotions_from'
    )
    to_rank = models.ForeignKey(
        Rank,
        on_delete=models.PROTECT,
        related_name='promotions_to'
    )
    approved_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name='approved_promotions'
    )
    approved_at = models.DateTimeField(auto_now_add=True)
    reason = models.TextField(blank=True)

    def __str__(self):
        return f'{self.player} - {self.from_rank} + {self.to_rank}'