import unittest
from unittest.mock import patch
import time
import threading
import TwitchConnect  # Assuming TwitchConnect is the module that contains your code

class TestTwitchStatistics(unittest.TestCase):

    def setUp(self):
        self.user_count = {}  # Reset user statistics before each test
        self.message_count = 0
        self.twitch_thread = threading.Thread(target=TwitchConnect.display_stats)
        self.twitch_thread.start()

    def tearDown(self):
        self.twitch_thread.join()

    @patch("TwitchConnect.user_count", {})
    @patch("TwitchConnect.message_count", 0)
    def test_join_and_part_actions(self):
        TwitchConnect.update_stats("JOIN #user1", "Hello, Twitch!")
        TwitchConnect.update_stats("JOIN #user2", "Welcome to the chat!")
        TwitchConnect.update_stats("PART #user1", "Goodbye, user1!")
        TwitchConnect.update_stats("PART #user3", "User3 left the chat")

        # Check user_count
        self.assertEqual(TwitchConnect.user_count, {"#user2": 1, "#user3": -1})

        # Check message_count
        self.assertEqual(TwitchConnect.message_count, 4)

    @patch("TwitchConnect.user_count", {})
    @patch("TwitchConnect.message_count", 0)
    def test_message_count(self):
        TwitchConnect.update_stats("JOIN #user1", "Hello, Twitch!")
        TwitchConnect.update_stats("JOIN #user2", "Welcome to the chat!")
        TwitchConnect.update_stats("PART #user1", "Goodbye, user1!")

        # Check user_count
        self.assertEqual(TwitchConnect.user_count, {"#user2": 1})

        # Check message_count
        self.assertEqual(TwitchConnect.message_count, 3)

if __name__ == '__main__':
    unittest.main()
