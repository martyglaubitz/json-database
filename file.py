import enum
import json

import os
import os.path

import configuration

def ensure_parentFolder(*path: str):
    abs_file_path = os.path.join(configuration.data_dir, path)
    dir_name = os.path.dirname(abs_file_path)
    if os.path.isdir(dir_name):
        return

    os.makedirs(dir_name)
    os.rename()



def file_for_path_exists(*path: str):
    return os.path.exists(os.path.join(configuration.data_dir, path))

def file_for_path(path: str, mode='r'):
    return open(os.path.join(configuration.data_dir, path), mode)

def delete_file_for_path(*path: str):
    os.remove(os.path.join(configuration.data_dir, path))

def json_for_path(*path: str):
    with file_for_path(os.path.join(configuration.data_dir, path)) as json_file:
        return json.load(json_file)

def create_folder(folder_name: str):
    os.mkdir(os.path.join(configuration.data_dir, folder_name))

def delete_folder(folder_name: str):
    os.rmdir(os.path.join(configuration.data_dir, folder_name))

def write_json_for_path(path: str, json_data: dict) -> WriteMode:
    with file_for_path(path) as json_file:
        return json.load(json_file)