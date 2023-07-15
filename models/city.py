#!/usr/bin/python3
"""
Module define clas City that inherits from BaseModel
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Intialise class city
    Attributes:
        state_id (string): empty
        name (string): empty
    """
    state_id = ""
    name = ""
