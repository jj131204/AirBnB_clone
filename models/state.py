#!/usr/bin/python3
""" State module """
from models.base_model import BaseModel


class State(BaseModel):
    """State class implementation"""

    name = ""

    def __init__(self, *args, **kwargs):
        """ Initialize in parent class """
        super().__init__(self, *args, **kwargs)
