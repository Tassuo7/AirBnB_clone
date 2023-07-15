#!/usr/bin/python3
"""
Module defines class User that inherits from BaseModel
"""


from models.base_model import BaseModel


class User(BaseModel):
    """
    Intialise class User
    Attributes:
    email(string)
    password(string)
    first_name(string)
    last_name(string)
    """
    first_name = ""
    last_name = ""
    email = ""
    password = ""
