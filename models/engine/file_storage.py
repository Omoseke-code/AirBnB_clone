#!/usr/bin/python3
"""File storage model"""
import json
from models.base_model import BaseModel

class FileStorage:
    """"Storage engine.
    Attributes:
        __file_path (str): The name of the file to save objects to.
         __objects (dict): A dictionary of instantiated objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        name = obj.__class.__name
        FileStorage.__objects["{name}.{obj.id}"] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path)"""
        dic = FileStorage.__objects
        todic = {obj: dic["obj"].to_dict for obj in dic.keys()}
        with open(FileStorage.__filepath, "w") as f:
            json.dump(todic, f)

    def reload(self):
        """deserializes the JSON file to __objects (only if the 
        JSON file (__file_path) exists otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised)
        """
        try:
            with open(FileStorage.__file_path) as f:
                ob = json.loads(f)
                for o in ob.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return
