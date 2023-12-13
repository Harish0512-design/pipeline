import json
import os

CONFIG_FILE_PATH = os.path.join(os.path.dirname(__file__), "config.json")


def read_config_file() -> dict:
    print("Reading config file")
    try:
        with open(CONFIG_FILE_PATH, "r") as file:
            data = json.load(file)
        return data
    except Exception as er:
        print(f"Failed to read config file: {er}")
        return {}


config_data = read_config_file()


def get_mongodb_configuration():
    print("Reading MongoDB configuration")
    try:
        result = config_data.get("MONGODB_CONFIGURATION", {})
        return result
    except Exception as er:
        print(f"Failed to read MongoDB configuration: {er}")
        return {}


def get_electric_vehicles_configuration():
    print("Reading electric vehicles configuration")
    try:
        result = config_data.get("URLS_AND_COLLECTIONS", {}).get("ELECTRIC_VEHICLES", {})
        return result
    except Exception as er:
        print(f"Failed to read Electric vehicles Configuration: {er}")
        return {}
