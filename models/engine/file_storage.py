#!/usr/bin/python3

import json
import models

class FileStorage:
    """
    A class for serializing instances to a JSON file and deserializing JSON file to instances.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id.
        """
        class_name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(class_name, obj.id)] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path).
        """
        serialized_objects = {}
        for key, obj in FileStorage.__objects.items():
            serialized_objects[key] = obj.to_dict()

        with open(FileStorage.__file_path, 'w') as f:
            json.dump(serialized_objects, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects.
        """
        try:
            with open(FileStorage.__file_path, 'r') as f:
                serialized_objects = json.load(f)
                for key, obj_dict in serialized_objects.items():
                    class_name, obj_id = key.split('.')
                    cls = getattr(models, class_name)  # Get the class by name
                    obj = cls(**obj_dict)  # Create an instance using class constructor
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass
