import sys
import os

# Add the parent directory to the system path to allow imports from the models package
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import unittest
from models.analytics import Analytics
from models.habit import Habit

class TestAnalytics(unittest.TestCase):
    """
    Unit tests for the Analytics class.
    """

    def test_longest_streak(self):
        """
        Test the longest_streak method of the Analytics class.

        Scenario:
        - Two habits are created with streaks of 5 and 3.
        - Expected result: The longest streak is 5.
        """
        # Create test habits with different streaks
        habits = [Habit("Exercise", "daily"), Habit("Read", "weekly")]
        habits[0].current_streak = 5  # Assign streak of 5 to the first habit
        habits[1].current_streak = 3  # Assign streak of 3 to the second habit

        # Assert that the longest streak is correctly identified as 5
        self.assertEqual(Analytics.longest_streak(habits), 5)

    def test_list_daily_habits(self):
        """
        Test the list_daily_habits method of the Analytics class.

        Scenario:
        - One daily habit and one weekly habit are created.
        - Expected result: The list contains only the name of the daily habit.
        """
        # Create test habits with different periodicities
        habits = [Habit("Exercise", "daily"), Habit("Read", "weekly")]

        # Assert that only the daily habit is listed
        self.assertEqual(Analytics.list_daily_habits(habits), ["Exercise"])

if __name__ == "__main__":
    # Run the unit tests
    unittest.main()
