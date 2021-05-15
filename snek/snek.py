
""" 
Main module of snek. Handles the setup and configuration of the database
"""

import os
import json

from .storage import Storage

class Snek:

    def __init__(self, path: str, mode="r+", create_dir=False):

        self._storage = Storage(path, mode, create_dir)


    def insert(self, data: dict):
        
        if not isinstance(data, dict):
            raise ValueError("Data is not dict")

        database = self._storage.read()

        if data is None:
            return
        else:
            return database

        def update(database: list):

            database.append(data)

    def get_all(self):

        return self._storage.read()

    @property
    def storage(self) -> Storage:

        return self._storage
    

    def __enter__(self):

        return self


    def __exit__(self):

        if self._open:
            self.storage.close()