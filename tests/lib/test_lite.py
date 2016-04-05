import mock
import unittest
from contextio.lib.lite import Lite

# from contextio.lib import errors
from contextio.lib.resources.user import User
# from contextio.lib.resources.connect_token import ConnectToken
# from contextio.lib.resources.discovery import Discovery
# from contextio.lib.resources.oauth_provider import OauthProvider

class TestLite(unittest.TestCase):
    def setUp(self):
        self.api = Lite(consumer_key="foo", consumer_secret="bar", version="lite")

    @mock.patch("contextio.lib.api.Api._request_uri")
    def test_get_users_returns_a_list_of_User_resources(self, mock_request):
        mock_request.return_value = {"id": "some_id"}
        accounts = self.api.get_users()

        self.assertEqual(1, len(accounts))
        self.assertIsInstance(accounts[0], User)

    @mock.patch("contextio.lib.api.Api._request_uri")
    def test_post_user_returns_User(self, mock_request):
        mock_request.return_value = {"id": "some_id"}

        user = self.api.post_user(email="fake@email.com")

        self.assertIsInstance(user, User)

