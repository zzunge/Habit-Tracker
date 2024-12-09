import datetime

class Habit:
    """
    Represents a habit tracked by the user.

    Attributes:
        name (str): The name of the habit.
        periodicity (str): The frequency of the habit ('daily' or 'weekly').
        creation_date (datetime.date): The date the habit was created.
        completion_history (list): A list of dates when the habit was marked as complete.
        current_streak (int): The current streak of consecutive completions.
    """

    def __init__(self, name, periodicity):
        """
        Initialize a new Habit instance.

        Args:
            name (str): The name of the habit.
            periodicity (str): The frequency of the habit ('daily' or 'weekly').
        """
        self.name = name
        self.periodicity = periodicity  # "daily" or "weekly"
        self.creation_date = datetime.date.today()
        self.completion_history = []  # Stores dates when the habit was completed
        self.current_streak = 0  # Tracks the current streak of consecutive completions

    def mark_complete(self):
        """
        Mark the habit as complete for today.
        If today is not already in the completion history, add it and update the streak.
        """
        today = datetime.date.today()
        if today not in self.completion_history:
            self.completion_history.append(today)
            self.update_streak(today)

    def update_streak(self, date):
        """
        Update the streak based on the periodicity of the habit.

        Args:
            date (datetime.date): The date when the habit was completed.
        """
        # Determine the expected date for the previous completion
        if self.periodicity == "daily":
            expected_date = date - datetime.timedelta(days=1)
        elif self.periodicity == "weekly":
            expected_date = date - datetime.timedelta(weeks=1)

        # Check if the previous completion matches the expected date
        if len(self.completion_history) > 1 and self.completion_history[-2] == expected_date:
            self.current_streak += 1
        else:
            self.current_streak = 1

    def is_broken(self):
        """
        Check if the habit is considered 'broken' (not completed on time).

        Returns:
            bool: True if the habit is broken, False otherwise.
        """
        today = datetime.date.today()
        if not self.completion_history:  # No completion history means the habit is broken
            return True
        last_completion = self.completion_history[-1]

        # Determine if the habit is broken based on periodicity
        if self.periodicity == "daily":
            return (today - last_completion).days > 1
        elif self.periodicity == "weekly":
            return (today - last_completion).days > 7

    def to_dict(self):
        """
        Convert the Habit object to a dictionary for serialization.

        Returns:
            dict: A dictionary representation of the Habit object.
        """
        return {
            "name": self.name,
            "periodicity": self.periodicity,
            "creation_date": str(self.creation_date),  # Convert date to string
            "completion_history": [str(date) for date in self.completion_history],  # Convert dates to strings
            "current_streak": self.current_streak,
        }

    @staticmethod
    def from_dict(data):
        """
        Create a Habit object from a dictionary.

        Args:
            data (dict): A dictionary containing habit data.

        Returns:
            Habit: A Habit object populated with the data from the dictionary.
        """
        habit = Habit(data["name"], data["periodicity"])
        habit.creation_date = datetime.date.fromisoformat(data["creation_date"])  # Parse date from string
        habit.completion_history = [datetime.date.fromisoformat(d) for d in data["completion_history"]]
        habit.current_streak = data["current_streak"]
        return habit
