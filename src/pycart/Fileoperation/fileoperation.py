import json


def get_data(json_path):
    """
    takes input path as json file and returns json data
    :param json_path:
    :return json data in dictionary format:
    """
    with open(json_path) as file:
        data = json.load(file)
    return data


def update_data(json_path, current_update: dict):
    """
    Updating the Particular key value pair
    :param json_path:
    :param current_update:
    """
    with open(json_path, 'r+') as f:
        json_data = json.load(f)
        for flower, qty in current_update.items():
            json_data[flower] = qty
        f.seek(0)
        f.write(json.dumps(json_data))
        f.truncate()
