import datetime

class Analytics:
    """
    Provides analytical features for habits, such as identifying longest streaks,
    challenging habits, and categorizing habits based on periodicity.
    """

    @staticmethod
    def longest_streak(habits):
        """
        Calculate the longest streak among all habits.

        Args:
            habits (list): A list of Habit objects.

        Returns:
            int: The longest streak value. If no habits exist, returns 0.
        """
        return max((habit.current_streak for habit in habits), default=0)

    @staticmethod
    def most_challenging_habits(habits):
        """
        Identify the habits that are currently broken (not completed).

        Args:
            habits (list): A list of Habit objects.

        Returns:
            list: A list of habit names that are broken.
        """
        return [habit.name for habit in habits if habit.is_broken()]

    @staticmethod
    def list_daily_habits(habits):
        """
        List all habits with a daily periodicity.

        Args:
            habits (list): A list of Habit objects.

        Returns:
            list: A list of habit names with daily periodicity.
        """
        return [habit.name for habit in habits if habit.periodicity == "daily"]

    @staticmethod
    def list_weekly_habits(habits):
        """
        List all habits with a weekly periodicity.

        Args:
            habits (list): A list of Habit objects.

        Returns:
            list: A list of habit names with weekly periodicity.
        """
        return [habit.name for habit in habits if habit.periodicity == "weekly"]

    @staticmethod
    def habits_broken_last_month(habits):
        """
        Identify habits that were broken within the last 30 days.

        Args:
            habits (list): A list of Habit objects.

        Returns:
            list: A list of habit names that were broken and created within the last month.
        """
        one_month_ago = datetime.date.today() - datetime.timedelta(days=30)
        return [
            habit.name
            for habit in habits
            if habit.is_broken() and habit.creation_date >= one_month_ago
        ]
