from django.test import TestCase

from users_app.models import User
from users_app.api.serializers import UserSerializer


class UserAPITestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="TestUser",
            password="TestPassword123",
            callsign="TestCallsign",
            discord_id="123456789"
        )

    def test_user_serializer(self):
        serialized_user = UserSerializer(
            self.user
        )
        data = serialized_user.data
        self.assertEqual(
            "TestUser",
            data["username"]
        )
        self.assertEqual(
            "TestCallsign",
            data["callsign"]
        )
        self.assertEqual(
            "123456789",
            data["discord_id"]
        )
        self.assertNotIn(
            "password",
            data
        )
        self.assertEqual(
            0, data["xp"]
        )
        self.assertEqual(
            "PV1",
            data["rank"]
        )