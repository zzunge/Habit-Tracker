import click
from models.habit import Habit
from models.user import User
from models.analytics import Analytics
import json

user_data_file = "data/user_data.json"

def save_user(user):
    with open(user_data_file, "w") as f:
        json.dump(user.to_dict(), f)

def load_user():
    try:
        with open(user_data_file, "r") as f:
            data = json.load(f)
            return User.from_dict(data)
    except (FileNotFoundError, json.JSONDecodeError):
        user = User("DefaultUser")
        save_user(user)
        return user

def habit_tracker_menu():
    while True:
        print("\nHabit Tracker Menu:")
        print("1. Add New Habit")
        print("2. Check-Off Habit")
        print("3. Streak Tracking")
        print("4. Analytics Features")
        print("5. Quit")
        
        choice = input("Enter choice: ")
        
        if choice == "1":
            add_new_habit()
        elif choice == "2":
            check_off_habit()
        elif choice == "3":
            show_streak_tracking()
        elif choice == "4":
            show_analytics_features()
        elif choice == "5":
            print("Exiting Habit Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

def add_new_habit():
   
    name = input("Enter new habit name: ")
    periodicity = input("Enter periodicity (daily/weekly): ")
    user = load_user()
    new_habit = Habit(name, periodicity)
    user.add_habit(new_habit)
    save_user(user)
    print(f"Habit '{name}' with periodicity '{periodicity}' added!")

def check_off_habit():
    
    name = input("Enter the name of the habit to check off: ")
    user = load_user()
    habit = user.get_habit(name)
    if habit:
        habit.mark_complete()
        save_user(user)
        print(f"Habit '{name}' marked as complete!")
    else:
        print(f"Habit '{name}' not found.")

def show_streak_tracking():
   
    user = load_user()
    for habit in user.habits:
        print(f"Habit: {habit.name}, Current Streak: {habit.current_streak}")

def show_analytics_features():
  
    user = load_user()
    print(f"Longest streak: {Analytics.longest_streak(user.habits)}")
    print(f"Most challenging habits: {Analytics.most_challenging_habits(user.habits)}")
    print(f"Daily habits: {Analytics.list_daily_habits(user.habits)}")
    print(f"Weekly habits: {Analytics.list_weekly_habits(user.habits)}")

if __name__ == "__main__":
    habit_tracker_menu()


