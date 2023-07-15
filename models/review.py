#!/usr/bin/python3
"""
module defines the Review class
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Intialise review
    Attributes:
        place_id (string): empty
        user_id (string): empty
        text (string): empty
    """
    place_id = ""
    user_id = ""
    text = ""
