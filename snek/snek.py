""" 
Main module of snek
"""

import os
import json
from storage import Storage

class Snek(Storage):

    storage = None

    def __init__(self, _dir):

        """
        create a storage object from here and map it
        to be used with snek
        """
        self.storage = Storage(_dir)

    def __repr__(self):

        """ 
        this returns some information about the object
        """

        # return '<{}>'.format(_storage._dir)
        return str(self)

    def __len__(self):
        """
        TODO add length of containers 
        """

        return 0