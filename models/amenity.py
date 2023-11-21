#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel


class Amenity(BaseModel):
    """ Amenity class of for the User """

    def __init__(self, *args, **kwargs):
        """ Does initialisation of attributes """
        super.__init__()
        self.name = kwargs.get('name', "")
