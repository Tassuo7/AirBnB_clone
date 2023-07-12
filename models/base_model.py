#!/usr/bin/python3
import uuid
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
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        obj_copy = self.__dict__.copy()
        obj_copy["__class__"] = self.__class__.__name__
        obj_copy["created_at"] = self.created_at.isoformat()
        obj_copy["updated_at"] = self.updated_at.isoformat()
        return obj_copy
