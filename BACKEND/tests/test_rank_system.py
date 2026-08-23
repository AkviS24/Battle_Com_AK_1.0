from django.test import TestCase

from ranks_app.models import Rank
from ranks_app.rank_system import (
    get_current_rank,
    get_next_rank,
    has_required_xp,
    is_promotion_available,
    promote_automatically,
    approve_promotion
)
from users_app.models import PlayerProfile, User



class RankSystemTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="TestUser",
            password="TestPassword123",
            callsign="TestCallsign",
            discord_id="123456789"
        )
        self.profile = PlayerProfile.objects.get(
            user=self.user
        )
        self.rank = Rank.objects.get(abbreviation="PV2")

        self.approver = User.objects.create_user(
                    username="Approver",
                    password="ApproverPassword",
                    callsign="ApproverCallsign",
                    discord_id="987654321"
                )

    def test_get_current_rank(self):
        current_rank = get_current_rank(self.profile)

        self.assertEqual(current_rank, self.profile.current_rank)

    def test_get_next_rank(self):
        next_rank = get_next_rank(self.profile)

        self.assertEqual(next_rank.abbreviation, "PV2")

    def test_has_required_xp(self):
        self.profile.xp = 100

        self.assertTrue(has_required_xp(self.profile, self.rank))

    def test_has_not_required_xp(self):
        self.profile.xp = 99

        self.assertFalse(has_required_xp(self.profile, self.rank))

    def test_promotion_available(self):
        self.profile.xp = 100

        self.assertTrue(
            is_promotion_available(self.profile)
        )

    def test_promotion_not_available(self):
        self.profile.xp = 99

        self.assertFalse(
            is_promotion_available(self.profile)
        )

    def test_no_promotion_available_at_highest_rank(self):
        highest_rank = Rank.objects.get(
            abbreviation="SMA"
        )

        self.profile.current_rank = highest_rank
        self.profile.save()

        self.assertFalse(
            is_promotion_available(self.profile)
        )

    def test_promote_automatically(self):
        self.profile.xp = 100

        promote_automatically(self.profile)

        self.assertEqual(
            self.profile.current_rank.abbreviation,
            "PV2"
        )

    def test_promote_automatically_multiple_ranks(self):
        self.profile.xp = 1000

        promote_automatically(self.profile)

        self.assertEqual(
            self.profile.current_rank.abbreviation,
            "CPL"
        )

    def test_promote_automatically_stops_at_approval_rank(self):
        self.profile.current_rank = Rank.objects.get(
            abbreviation="CPL"
        )
        self.profile.xp = 1500

        promote_automatically(self.profile)

        self.assertEqual(
            self.profile.current_rank.abbreviation,
            "CPL"
        )

    def test_approve_promotion(self):
        self.approver.profile.current_rank = Rank.objects.get(
            abbreviation="SMA"
        )
        self.approver.profile.save()
        self.profile.current_rank = Rank.objects.get(
            abbreviation="CPL"
        )
        self.profile.xp = 1500
        self.profile.save()

        promotion = approve_promotion(
            self.profile,
            self.approver
        )

        self.assertIsNotNone(promotion)

    def test_approve_promotion_only_sma(self):
        self.profile.current_rank = Rank.objects.get(
            abbreviation="CPL"
        )
        self.profile.xp = 1500
        self.profile.save()

        promotion = approve_promotion(
            self.profile,
            self.approver
        )

        self.assertIsNone(promotion)