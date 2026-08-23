from rest_framework import serializers

from users_app.models import User


class UserSerializer(serializers.ModelSerializer):
    xp = serializers.IntegerField(
        source="profile.xp",
        read_only=True
    )
    rank = serializers.CharField(
        source="profile.current_rank.abbreviation",
        read_only=True,
    )

    class Meta:
        model = User
        fields = [
            "username",
            "callsign",
            "discord_id",
            "xp",
            "rank",
        ]