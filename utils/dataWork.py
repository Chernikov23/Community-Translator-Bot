import json
from threading import Lock

user_data_lock = Lock()


def load_user_data():
    with user_data_lock:
        try:
            with open('utils/user_data.json', 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

def save_user_data(user_data):
    with user_data_lock:
        with open('utils/user_data.json', 'w') as file:
            json.dump(user_data, file, ensure_ascii=False, indent=4)


user_data_file_path = 'utils/user_data.json'

try:
    with open(user_data_file_path, 'r') as file:
        user_data = json.load(file)
    print("ВСЕ ОТЛИЧНО")
except FileNotFoundError:
    user_data = {}
    with open(user_data_file_path, 'w') as file:
        json.dump(user_data, file)
except json.JSONDecodeError:
    print(f"Файл {user_data_file_path} поврежден или не является валидным JSON.")