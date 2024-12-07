import datetime

class Analytics:
    @staticmethod
    def longest_streak(habits):
        return max((habit.current_streak for habit in habits), default=0)

    @staticmethod
    def most_challenging_habits(habits):
        return [habit.name for habit in habits if habit.is_broken()]

    @staticmethod
    def list_daily_habits(habits):
        return [habit.name for habit in habits if habit.periodicity == "daily"]

    @staticmethod
    def list_weekly_habits(habits):
        return [habit.name for habit in habits if habit.periodicity == "weekly"]

    @staticmethod
    def habits_broken_last_month(habits):
        one_month_ago = datetime.date.today() - datetime.timedelta(days=30)
        return [
            habit.name
            for habit in habits
            if habit.is_broken() and habit.creation_date >= one_month_ago
        ]
