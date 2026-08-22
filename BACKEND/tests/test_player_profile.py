from django.test import TestCase

from ranks_app.models import Rank
from users_app.models import User, PlayerProfile


class PlayerProfileTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="TestUser",
            password="TestPassword123",
            callsign="TestCallsign",
            discord_id="123456789"
        )
        self.player_profile = PlayerProfile.objects.get(
                    user=self.user
                )

    def test_player_profile_creation(self):
        self.assertEqual(self.player_profile.user, self.user)

    def test_player_profile_default_xp(self):
        self.assertEqual(self.player_profile.xp, 0)

    def test_player_profile_default_rank(self):
        self.assertEqual(self.player_profile.current_rank.abbreviation, "PV1")