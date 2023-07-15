#!/usr/bin/python3
"""
Module defines class Place that inherits from BaseModel
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    Intialise a place.
    Attributes:
        city_id (string): empty
        user_id (str): empty
        name (str): Empty
        description (str): Empty
        number_rooms (int): 0 integer
        number_bathrooms (int): 0
        max_guest (int): 0
        price_by_night (int): default 0
        latitude (float): 0.0
        longitude (float): 0.0
        amenity_ids (list): EMPTY LIst of string
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
