#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel


class City(BaseModel):
    """ The city class, contains state ID and name """
    
    def __init__(self, *args, **kwargs):
        """ Initialises attributes of class City """
        super().__init__()
        self.state_id = kwargs.get('state_id', "")
        self.name = kwargs.get('name', "")
