#!/usr/bin/python3
"""Defines the BaseModel class."""
import models
from uuid import uuid4
from datetime import datetime

class BaseModel:
    """The base model to the models in this package"""

    def __init__(self, *args, **kwargs):
        """Intialises the basemodel
        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        timeform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, timeform)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def save(self):
        """updates the public instance attribute updated_at
        with the current datetime"""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of
        __dict__ of the instance"""
        retdict = self.__dict__.copy()
        retdict['created_at'] = self.created_at.isoformat()
        retdict['updated_at'] = self.updated_at.isoformat()
        retdict['__class__'] = self.__class__.__name__
        return retdict

    def __str__(self):
        """Returns the string form of the class
        Args:
            id (str): id of the instance
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
