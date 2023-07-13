#!/usr/bin/python3
import json


class FileStorage:
    """ Class to define the storage class
        Artributes:
            __file_path = contains the path to the file
            __objects = private atttribute to store the all objects
        Methods:
            all: return all the object in the __objects attributes
            new: add an new object to the __objects
            class: import all classes to be instanciated
            save: save all the object instances to a json file
            reload: load all the data from the file to __objects in the exit
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns all the objects in the __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """add a new object to __objects"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def classes(self):
        """contains all class to use for instanciating an object"""
        from models.base_model import BaseModel
        classes = {"BaseModel": BaseModel}
        return classes

    def save(self):
        """save the attribute of each instance to a file"""
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            u = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(u, file)

    def reload(self):
        """loads the attributes from from the file to objects"""
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                data = json.load(file)
            for k, v in data.items():
                class_name, obj_id = k.split(".")
                cls = self.classes().get(class_name)
                if cls:
                    obj = cls(**v)
                    FileStorage.__objects[k] = obj
        except FileNotFoundError:
            return
