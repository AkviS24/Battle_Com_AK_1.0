from django.test import TestCase

from rest_framework.test import (
    APIRequestFactory,
    force_authenticate
)

from users_app.models import User
from users_app.api.views import CurrentUserView



class CurrentUserViewTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="TestUser",
            password="TestPassword123",
            callsign="TestCallsign",
            discord_id="123456789"
        )
        self.factory = APIRequestFactory()

    def test_current_user_authenticated(self):
        request = self.factory.get("/api/users/me/")
        force_authenticate(
            request,
            user=self.user
        )
        view = CurrentUserView.as_view()
        response = view(request)

        self.assertEqual(
            200,
            response.status_code
        )
        self.assertEqual(
            "TestUser",
            response.data["username"]
        )
        self.assertEqual(
            "TestCallsign",
            response.data["callsign"]
        )
        self.assertEqual(
            "123456789",
            response.data["discord_id"]
        )
        self.assertEqual(
            0,
            response.data["xp"]
        )
        self.assertEqual(
            "PV1",
            response.data["rank"]
        )

    def test_current_user_unauthenticated(self):
        request = self.factory.get("/api/users/me/")
        view = CurrentUserView.as_view()
        response = view(request)

        self.assertEqual(
            403,
            response.status_code
        )