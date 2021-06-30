#!/usr/bin/python3
""" BaseModel Class """

import uuid
from datetime import datetime
import models


class BaseModel:
    """
    - Defines all common attributes/methods for other classes.
    """
    def __init__(self, *args, **kwargs):
        """ Initialize an instance of BaseModel. """
        if kwargs:
            for key, value in kwargs.items():

                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(value,
                            "%Y-%m-%dT%H:%M:%S.%f"))

                elif key != "__class__":
                    setattr(self, key, value)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """ Return a representation of the class. """
        name = self.__class__.__name__
        return "[{}] ({}) {}".format(name, self.id, self.__dict__)

    def save(self):
        """
        - Updates the public instance attribute ``updated_at``
          with the current datetime.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        - Returns a dictionary containing all keys/values
          of __dict__ of the instance.
        """
        representation = self.__dict__.copy()
        representation["updated_at"] = self.updated_at.isoformat()
        representation["created_at"] = self.created_at.isoformat()
        representation["__class__"] = self.__class__.__name__
        return representation
