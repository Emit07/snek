""" 
Main module of snek
"""

import os
import json
from snek.storage import Storage
import snek.config as config

class Snek(Storage):

    def __init__(self, _dir):

        """
        create a config object from here and map it
        to be used with snek
        TODO map this to a config object
        """

        config.__dir__ = _dir

    def __repr__(self):

        """ 
        this returns some information about the object
        TODO add more info
        """

        return "<{}>".format(config.__dir__)

    def __len__(self):
        """
        TODO add length of containers 
        """

        return 0