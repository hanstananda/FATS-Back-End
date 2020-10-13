import os
import shutil
import uuid

from fats.settings import BASE_DIR


STORAGE_DIR = os.path.join(BASE_DIR, 'storage')
os.makedirs(STORAGE_DIR, exist_ok=True)


def random_file_name(extension):
    return uuid.uuid4().hex + extension


def store_temp_file(data, extension):
    file_name = os.path.join(STORAGE_DIR, 'temp', random_file_name(extension))
    create_directory('temp')
    with open(file_name, "wb") as f:
        f.write(data)
    return file_name


def create_directory(dir_name):
    full_path = os.path.join(STORAGE_DIR, str(dir_name))
    if os.path.exists(full_path):
        return False
    os.makedirs(full_path)
    return True
