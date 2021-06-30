#!/usr/bin/python3
"""user module"""

from models.base_model import BaseModel


class User(BaseModel):
    """User class implementation"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """ Initialize in parent class """
        super().__init__(self, *args, **kwargs)
