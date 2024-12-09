import sys
import os

# Add the parent directory to the system path to allow imports from the models package
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import unittest
from models.user import User
from models.habit import Habit

class TestUser(unittest.TestCase):
    """
    Unit tests for the User class.
    """

    def test_add_habit(self):
        """
        Test the add_habit method of the User class.

        Scenario:
        - Create a user and add a habit to their habit list.
        - Expected result: The habit list contains one habit after adding.
        """
        # Create a user and a habit instance
        user = User("TestUser")
        habit = Habit("Exercise", "daily")

        # Add the habit to the user's habit list
        user.add_habit(habit)

        # Assert that the habit list contains one habit
        self.assertEqual(len(user.habits), 1)

    def test_remove_habit(self):
        """
        Test the remove_habit method of the User class.

        Scenario:
        - Add a habit to a user's habit list and then remove it by name.
        - Expected result: The habit list is empty after removing the habit.
        """
        # Create a user and a habit instance
        user = User("TestUser")
        habit = Habit("Exercise", "daily")

        # Add the habit to the user's habit list
        user.add_habit(habit)

        # Remove the habit from the user's habit list by name
        user.remove_habit("Exercise")

        # Assert that the habit list is empty
        self.assertEqual(len(user.habits), 0)

if __name__ == "__main__":
    # Run the unit tests
    unittest.main()
