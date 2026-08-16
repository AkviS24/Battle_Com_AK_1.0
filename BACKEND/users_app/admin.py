from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


from .models import PlayerProfile, User

# Register your models here.


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Battle Com', {
            'fields': ('callsign', 'discord_id'),
        }),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Battle Com', {
            'fields': ('callsign', 'discord_id'),
        }),
    )


@admin.register(PlayerProfile)
class PlayerProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'xp')