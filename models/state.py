#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel


class State(BaseModel):
    """ State class """

    def __init__(self, *args, **kwargs):
        """ Initialises attributes of class State """
        super().__init__()
        self.name = kwargs.get('name', "")
