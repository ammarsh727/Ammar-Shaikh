import json

# Path to the JSON file where the perfume data will be stored
DATA_FILE = 'data/perfumes.json'

def load_data():
    """Load the perfume collection from the JSON file."""
    try:
        with open(DATA_FILE, 'r') as file:
            return [Perfume(**item) for item in json.load(file)]
    except FileNotFoundError:
        # If the file doesn't exist, return an empty list
        return []

def save_data(collection):
    """Save the perfume collection to the JSON file."""
    with open(DATA_FILE, 'w') as file:
        json.dump([perfume.__dict__ for perfume in collection], file, indent=4)
