#!/usr/bin/python3
import uuid
from models import storage
from datetime import datetime
"""
This is module to defines BaseModel Class
"""


class BaseModel:
    """
    Initialise instance attributes
    attributes:
        public id :string - assign with an uuid when an instance is created:
        created_at: assign with the current datetime when an instance created
        updated_at: assign with the current datetime when an instance created
    Return: Nothing
    """
    def __init__(self, *args, **kwargs):
        """Initialisation"""
        date_f = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "updated_at" or key == "created_at":
                    self.__dict__[key] = datetime.strptime(value, date_f)
                else:
                    self.__dict__[key] = value

    def __str__(self):
        """print str format"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """updates the attribute updated_at with the current datetime"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values"""
        obj_copy = self.__dict__.copy()
        obj_copy["__class__"] = self.__class__.__name__
        obj_copy["created_at"] = self.created_at.isoformat()
        obj_copy["updated_at"] = self.updated_at.isoformat()
        return obj_copy
