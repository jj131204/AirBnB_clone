#!/usr/bin/python3
""" Review module  """
from models.base_model import BaseModel


class Review(BaseModel):
    """ Review class implementation"""

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """ Initialize in parent class """
        super().__init__(self, *args, **kwargs)
