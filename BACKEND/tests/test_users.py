from django.test import TestCase


from users_app.models import User


class UserTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="TestUser",
            password="TestPassword123",
            callsign="TestCallsign",
            discord_id="123456789"
        )

    def test_user_creation(self):
        self.assertEqual(self.user.username, "TestUser")
        self.assertEqual(self.user.callsign, "TestCallsign")
        self.assertEqual(self.user.discord_id, "123456789")

    def test_user_password(self):
        self.assertNotEqual(self.user.password, "TestPassword123")
        self.assertTrue(self.user.check_password("TestPassword123"))
        self.assertFalse(self.user.check_password("wrongPassword"))