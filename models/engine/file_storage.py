#!/usr/bin/python3
"""
module to defines class FileStorage
"""
import json
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
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
                    class_n = obj_atr['__class__']
                    del obj_atr['__class__']
                    FileStorage.__objects[k] = eval(class_n)(**obj_atr)
        except FileNotFoundError:
            return
