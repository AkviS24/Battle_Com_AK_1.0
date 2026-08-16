from django.contrib import admin

from .models import Promotion, Rank


# Register your models here.
@admin.register(Rank)
class RankAdmin(admin.ModelAdmin):
    list_display = (
        'order',
        'name',
        'abbreviation',
        'min_xp',
        'category',
        'requires_approval',
    )
    ordering = ('order',)


@admin.register(Promotion)
class PromotionAdmin(admin.ModelAdmin):
    list_display = (
        'player',
        'from_rank',
        'to_rank',
        'approved_by',
        'approved_at',
    )