#!/usr/bin/python3
"""
module to defines class FileStorage
"""
import json


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
        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key
        """
        k = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[k] = obj

    def save(self):
        """
        serializes __objects to the JSON file
        """
        obj_d = {k: obj.to_dict() for k, obj in self.__objects.items()}
        with open(self.__file_path, "w") as fl:
            json.dump(obj_d, fl)

    def reload(self):
        try:
            with open(self.__file_path, "r") as fl:
                ob_d = json.load(fl)
                for k, obj_atr in ob_d.items():
                    class_n, obj_id = key.split(".")
                    class_m = eval(class_n)
                    o = class_m(**obj_atr)
                    self.__objects[k] = o
        except FileNotFoundError:
            return
