from models.habit import Habit

class User:
    """
    Represents a user in the Habit Tracker application.

    Attributes:
        username (str): The username of the user.
        habits (list): A list of Habit objects associated with the user.
    """

    def __init__(self, username):
        """
        Initialize a new User instance.

        Args:
            username (str): The username of the user.
        """
        self.username = username
        self.habits = []  # List to store the user's habits

    def add_habit(self, habit):
        """
        Add a new habit to the user's habit list.

        Args:
            habit (Habit): A Habit object to add to the user's habit list.
        """
        self.habits.append(habit)

    def remove_habit(self, habit_name):
        """
        Remove a habit from the user's habit list by its name.

        Args:
            habit_name (str): The name of the habit to remove.
        """
        self.habits = [habit for habit in self.habits if habit.name != habit_name]

    def get_habit(self, habit_name):
        """
        Retrieve a habit by its name.

        Args:
            habit_name (str): The name of the habit to retrieve.

        Returns:
            Habit or None: The habit with the specified name, or None if not found.
        """
        for habit in self.habits:
            if habit.name == habit_name:
                return habit
        return None

    def to_dict(self):
        """
        Convert the User object to a dictionary for serialization.

        Returns:
            dict: A dictionary representation of the User object.
        """
        return {
            "username": self.username,
            "habits": [habit.to_dict() for habit in self.habits],  # Serialize each habit
        }

    @staticmethod
    def from_dict(data):
        """
        Create a User object from a dictionary.

        Args:
            data (dict): A dictionary containing user data.

        Returns:
            User: A User object populated with the data from the dictionary.
        """
        user = User(data["username"])  # Create a new User with the username
        user.habits = [Habit.from_dict(h) for h in data["habits"]]  # Deserialize habits
        return user
