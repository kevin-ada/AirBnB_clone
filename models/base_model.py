#!/usr/bin/python3
"""Defines the Base class model."""
from datetime import datetime
import models
from uuid import uuid4


class BaseModel:
    """Represents the BaseModel of the AirBnB project."""

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel.
        """
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.now()
        if kwargs is not None:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, tform)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

        def __str__(self):
            """print a base model"""
            return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

        def save(self):
            """Update updated_at with the current time."""
            self.updated_at = datetime.today()
            models.storage.save()

        def to_dict(self):
            """Return the dictionary representation
            of the BaseModel instance.
            """
            rdict = self.__dict__.copy()
            rdict["created_at"] = self.created_at.isoformat()
            rdict["updated_at"] = self.updated_at.isoformat()
            rdict["__class__"] = self.__class__.__name__
            return rdict
