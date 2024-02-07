#!/usr/bin/python3

import datetime
import uuid
import models


class BaseModel:
    """
    A base class representing a generic model with common attributes
    """

    def __init__(self, *args, **kwargs):
        """
            Initializes a new instance of the BaseModel class.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key == 'created_at' or key == 'updated_at':
                        setattr(self, key, datetime.datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))
                    else:
                        setattr(self, key, value)
        else:
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            self.id = str(uuid.uuid4())

    def __str__(self):
        """
        Returns a string representation of the BaseModel instance.

        Returns:
            str: A string representation containing the class name
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
            dict: A dictionary containing all the instance attrib
        """
        class_name = self.__class__.__name__
        obj_dict = self.__dict__.copy()

        obj_dict['__class__'] = class_name
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
