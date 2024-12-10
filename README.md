# Habit-Tracker

A simple app to help you track and analyze your habits!

## Features
- Add and manage daily or weekly habits.
- Track streaks and visualize performance.
- Analyze your most consistent and challenging habits.

## Tech Stack

- **Language**: Python
- **Database**: JSON
- **Testing**: Unittest
- **Environment**: Virtualenv

![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white)
![JSON](https://img.shields.io/badge/-JSON-000000?logo=json&logoColor=white)
![Unittest](https://img.shields.io/badge/-Unittest-0078D4)


## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/zzunge/Habit-Tracker.git
   cd Habit-Tracker
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   python main.py

## Usage 


## Testing

This project includes unit tests to verify the functionality of core features.
To run all unit tests, use the following command:

```bash
python -m unittest discover -s tests
```
## Data Structure
Habits and user data are stored in JSON format. Here's an example:
```json
{
  "username": "DefaultUser",
  "habits": [
    {
      "name": "Exercise",
      "periodicity": "daily",
      "creation_date": "2024-12-01",
      "completion_history": ["2024-12-01", "2024-12-02"],
      "current_streak": 2
    }
  ]
}
```




