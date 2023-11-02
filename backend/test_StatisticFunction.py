import StatisticFunction as StatisticFunction;
import unittest
from StatisticFunction import update_stats, user_count, message_count

class TestStatisticsFunction(unittest.TestCase):

    def setUp(self):
        user_count = 0
        message_count = 0

    def test_update_stats_join(self):
        update_stats("JOIN #user1", "Uer joined")
        self.assertEqual(user_count, 1)
        self.assertEqual(message_count, 1)

    def test_update_stats_part(self):
        update_stats("PART #user2", "User left")
        self.assertEqual(user_count, -1)
        self.assertEqual(message_count, 1)

    def test_update_stats_other_message(self):
        update_stats("USER #user3", "Third cases")
        self.assertEqual(user_count, 0)
        self.assertEqual(message_count, 1)

if __name__ == '__main__':
    unittest.main()
