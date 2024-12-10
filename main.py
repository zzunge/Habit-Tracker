
from models.habit import Habit
from models.user import User
from models.analytics import Analytics
import json

# Path to the file where user data is stored
user_data_file = "data/user_data.json"

# Function to save user data to a JSON file
def save_user(user):
    """
    Save the user's data to the JSON file.

    Args:
        user (User): The user object to save.
    """
    with open(user_data_file, "w") as f:
        json.dump(user.to_dict(), f)

# Function to load user data from a JSON file
def load_user():
    """
    Load the user's data from the JSON file. 
    If the file doesn't exist or is corrupted, create a new user.

    Returns:
        User: The loaded or newly created user object.
    """
    try:
        with open(user_data_file, "r") as f:
            data = json.load(f)
            return User.from_dict(data)
    except (FileNotFoundError, json.JSONDecodeError):
        # If file not found or JSON is invalid, create a default user
        user = User("DefaultUser")
        save_user(user)
        return user

# Main menu for the Habit Tracker application
def habit_tracker_menu():
    """
    Display the main menu for the Habit Tracker and handle user input.
    """
    while True:
        print("\nHabit Tracker Menu:")
        print("1. Add New Habit")
        print("2. Check-Off Habit")
        print("3. Streak Tracking")
        print("4. Analytics Features")
        print("5. Quit")
        
        choice = input("Enter choice: ")
        
        # Handle user choice
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

# Function to add a new habit for the user
def add_new_habit():
    """
    Prompt the user to add a new habit with a name and periodicity.
    """
    name = input("Enter new habit name: ")
    periodicity = input("Enter periodicity (daily/weekly): ")
    user = load_user()
    new_habit = Habit(name, periodicity)
    user.add_habit(new_habit)
    save_user(user)
    print(f"Habit '{name}' with periodicity '{periodicity}' added!")

# Function to mark a habit as complete
def check_off_habit():
    """
    Prompt the user to mark a specific habit as complete.
    """
    name = input("Enter the name of the habit to check off: ")
    user = load_user()
    habit = user.get_habit(name)
    if habit:
        habit.mark_complete()
        save_user(user)
        print(f"Habit '{name}' marked as complete!")
    else:
        print(f"Habit '{name}' not found.")

# Function to display streak tracking information for all habits
def show_streak_tracking():
    """
    Display the current streak for each habit.
    """
    user = load_user()
    for habit in user.habits:
        print(f"Habit: {habit.name}, Current Streak: {habit.current_streak}")

# Function to display various analytics features
def show_analytics_features():
    """
    Show analytics such as the longest streak, most challenging habits,
    and lists of daily and weekly habits.
    """
    user = load_user()
    print(f"Longest streak: {Analytics.longest_streak(user.habits)}")
    print(f"Most challenging habits: {Analytics.most_challenging_habits(user.habits)}")
    print(f"Daily habits: {Analytics.list_daily_habits(user.habits)}")
    print(f"Weekly habits: {Analytics.list_weekly_habits(user.habits)}")

# Entry point for the application
if __name__ == "__main__":
    habit_tracker_menu()
