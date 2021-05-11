
""" 
Main module of snek
"""

import os
import json
from snek.storage import Storage
import snek.config as config

class Snek:

    def __init__(self, path: str, mode="r+", create_dir=False):

        """
        create a config object from here and map it
        to be used with snek
        TODO map this to a config object
        """

        config.__dir__ = path

        self._documents = {}

        self._storage = Storage(path, mode, create_dir)


    def update_db(self, action, data=None):
        
        return 0

    def insert(self, data: dict) -> int:

        if not isinstance(data, dict):
            raise ValueError("Value is not dictionary type.")




    def __enter__(self):

        return self

    def __exit__(self):

        if self._open:
            self.storage.close()

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