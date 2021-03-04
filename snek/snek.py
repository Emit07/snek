""" 
Main module of snek
"""

import os
import json
from storage import Storage

class Snek():

    storage = None

    def __init__(self, _dir):

        """
        create a storage object from here and map it
        to be used with snek
        """

        self.storage = Storage(_dir)

    def insert(self, value : dict):

        """
        maps snek class to storage 
        TODO find a better way to do this
        """

        self.storage.insert(value)
    
    def remove(self, value : str):
        self.storage.remove(value)
    
    def __repr__(self):

        """ 
        this returns some information about the object
        """

        return '<{}>'.format(_storage._dir)

    def __len__(self):
        """
        TODO add length of containers 
        """

        return 0