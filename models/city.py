#!/usr/bin/python3
"""models/city"""
from models.base_model import BaseModel


class City(BaseModel):
    """city class which inherits from the Basemodel class """

    state_id = ""
    name = ""
