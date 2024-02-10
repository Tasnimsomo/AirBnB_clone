#!/usr/bin/python3

import datetime
import uuid


class BaseModel:
    """
    A base class representing a generic model with common attributes
    """

    def __init__(self, *args, **kwargs):
        """
            Initializes a new instance of the BaseModel class.
        """
        from models import storage
        if kwargs:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                        kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]
            else:
                self.created_at = datetime.datetime.now()
                self.updated_at = datetime.datetime.now()
                self.id = str(uuid.uuid4())
                storage.new(self)

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
        from models import storage
        self.updated_at = datetime.datetime.now()
        storage.save()

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
