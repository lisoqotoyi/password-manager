import unittest
from unittest.mock import patch
import json
import os

import manager as pm

TEST_FILE = "test_login_details.json"
pm.FILE = TEST_FILE


class TestPasswordManager(unittest.TestCase):

    def setUp(self):
        with open(TEST_FILE, "w") as f:
            json.dump({}, f)

    def tearDown(self):
        if os.path.exists(TEST_FILE):
            os.remove(TEST_FILE)

    @patch("builtins.input", side_effect=[
        "gmail",
        "user1",
        "Password1!"
    ])
    def test_add_password(self, mock_input):
        data = pm.load_data()
        pm.add_password(data)

        self.assertIn("gmail", data)
        self.assertEqual(data["gmail"]["username"], "user1")
        self.assertEqual(data["gmail"]["password"], "Password1!")

    @patch("builtins.input", side_effect=[
        "gmail",
        "2",
        "user1",
        "Password1!"
    ])
    def test_overwrite_site(self, mock_input):
        data = {"gmail": {"username": "old", "password": "old"}}

        pm.add_password(data)

        self.assertEqual(data["gmail"]["username"], "user1")
        self.assertEqual(data["gmail"]["password"], "Password1!")

    @patch("builtins.input", return_value="user1")
    def test_search_username(self, mock_input):
        data = {
            "gmail": {"username": "user1", "password": "Pass1!"},
            "facebook": {"username": "other", "password": "Pass2!"}
        }

        with patch("builtins.print") as mock_print:
            pm.search_by_username(data)
            self.assertTrue(mock_print.called)

    @patch("builtins.input", side_effect=["gmail", "y"])
    def test_delete_password(self, mock_input):
        data = {
            "gmail": {"username": "user1", "password": "Pass1!"}
        }

        pm.delete_password(data)

        self.assertNotIn("gmail", data)


if __name__ == "__main__":
    unittest.main()