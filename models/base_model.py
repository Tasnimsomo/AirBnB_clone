#!/usr/bin/python3

import datetime
import uuid

class BaseModel:
    """
    A base class representing a generic model with common attributes and methods.
    """

    def __init__(self):
        """
        Initializes a new instance of the BaseModel class.

        Attributes:
            id (str): A unique identifier generated using UUID.
            created_at (datetime): The datetime when the instance was created.
            updated_at (datetime): The datetime when the instance was last updated.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """
        Returns a string representation of the BaseModel instance.

        Returns:
            str: A string representation containing the class name, id, and attribute dictionary.
        """
        class_name = self.__class__.__name__
        return "[{}]({}){}".format(class_name, self.id, self.__dict__)

    def save(self):
        """
        Updates the 'updated_at' attribute with the current datetime.
        """
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """
        Returns a dictionary representation of the BaseModel instance.

        Returns:
            dict: A dictionary containing all the instance attributes and their values.
        """
        class_name = self.__class__.__name__
        obj_dict = self.__dict__.copy()

        obj_dict['__class__'] = class_name
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict

