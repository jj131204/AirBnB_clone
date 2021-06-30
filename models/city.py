#!/usr/bin/python3
""" City module """
from models.base_model import BaseModel


class City(BaseModel):
    """ City class implementation """

    name = ""
    state_id = ""

    def __init__(self, *args, **kwargs):
        """ Initialize in parent class """
        super().__init__(self, *args, **kwargs)
