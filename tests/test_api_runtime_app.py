import unittest
from unittest.mock import patch

import chalice.test

from api.runtime.app import app


class AppTestCase(unittest.TestCase):
    @patch.dict("chalicelib.helpers.os.environ", {"TABLE_NAME": "AppTestCase"})
    @patch("chalicelib.users.DynamoDBDatabase.get_user")
    def test_get_user_exists(self, mock_get_user):
        username = "john"
        user = {"username": username, "email": f"{username}@example.com"}
        mock_get_user.return_value = user
        with chalice.test.Client(app) as client:
            response = client.http.get(
                f"/users/{username}",
                headers={"Content-Type": "application/json"},
            )
        self.assertEqual(response.json_body, user)


if __name__ == '__main__':
    unittest.main()
