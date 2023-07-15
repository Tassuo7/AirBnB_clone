#!/usr/bin/python3
"""
module to defines class FileStorage
"""
import json
from models.base_model import BaseModel


class FileStorage:
    """
    class that serializes instances to a JSON
    file and deserializes JSON file to instances
    """
    __objects = {}
    __file_path = "file.json"

    def all(self):
        """
         returns the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key
        """
        k = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[k] = obj

    def save(self):
        """
        serializes __objects to the JSON file
        """
        obj_d = {k: obj.to_dict() for k, obj in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, "w") as fl:
            json.dump(obj_d, fl)

    def reload(self):
        try:
            with open(FileStorage.__file_path, "r") as fl:
                ob_d = json.load(fl)
                for k, obj_atr in ob_d.items():
                    class_n, obj_id = k.split(".")
                    class_m = globals()[class_n]
                    o = class_m(**obj_atr)
                    FileStorage.__objects[k] = o
        except FileNotFoundError:
            return
