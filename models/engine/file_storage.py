#!/usr/bin/python3
""" ... """

from models.base_model import BaseModel
from models.amenity import Amenity
from models.review import Review
from models.state import State
from models.place import Place
from models.city import City
from models.user import User
import json


class FileStorage:
    """
    ...
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns the dictionary ``__objects`` """
        return self.__objects

    def new(self, obj):
        """
        - Sets in ``__objects`` the ``obj`` with key ``<obj class name>.id``
        """
        key = obj.__class__.__name__ + "." + str(obj.id)
        self.__objects[key] = obj

    def save(self):
        """ Serializes ``__objects`` to the JSON file """
        new_dict = {}

        for key, value in self.__objects.items():
            new_dict[key] = value.to_dict()

        with open(self.__file_path, mode="w", encoding="utf-8") as json_file:
            json.dump(new_dict, json_file)

    def reload(self):
        """ Deserializes the JSON file to ``__objects`` """

        try:
            with open(self.__file_path, mode="r", encoding="utf-8") as file:
                json_file = json.load(file)

            for key, value in json_file.items():
                cls_name = value["__class__"]
                obj = eval(cls_name + "(**value)")
                self.__objects[key] = obj

        except FileNotFoundError:
            pass
