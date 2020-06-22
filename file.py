import enum
import json

import os
import os.path

import configuration

class WriteMode(enum.Enum):
    CREATE = 1
    UPDATE = 2

def file_for_path_exists(path: str):
    return os.path.exists(os.path.join(configuration.data_dir, path))

def file_for_path(path: str, mode='r'):
    return open(os.path.join(configuration.data_dir, path), mode)

def delete_file_for_path(path: str):
    os.remove(os.path.join(configuration.data_dir, path))

def json_for_path(path: str):
    with file_for_path(path) as json_file:
        return json.load(json_file)

def write_json_for_path(path: str, json_data: dict) -> WriteMode:
    with file_for_path(path) as json_file:
        return json.load(json_file)