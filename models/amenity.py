#!/usr/bin/python3
""" Amenity module """

from models.base_model import BaseModel


class Amenity(BaseModel):
    """ Amenity class implementation """

    name = ""

    def __init__(self, *args, **kwargs):
        """ Initialize in parent class """
        super().__init__(self, *args, **kwargs)
