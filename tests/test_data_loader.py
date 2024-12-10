import json
import os

def load_test_data():
    """
    Load test data from the test_data.json file located in the test_data folder.
    """
    test_data_path = os.path.join(os.path.dirname(__file__), "test_data", "test_data.json")
    with open(test_data_path, "r") as f:
        data = json.load(f)
    return data
