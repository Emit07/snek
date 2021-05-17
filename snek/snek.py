
""" 
Main module of snek. Handles the setup and configuration of the database
"""

import os
import json

from .storage import Storage

class Snek:

    def __init__(self, *args, **kwargs):
        """
        Initiates the snek database
        """

        # Creates a storage object to interact with the database file
        self._storage = Storage(*args, **kwargs)

        self._open = True

    def insert(self, data: dict):
        """
        Inserts a single object into the database.
        """

        # Returns an error if the object is not a dictionary
        if not isinstance(data, dict):
            # TODO rewrite a better error message
            raise ValueError("Data is not dict")

        # Create a function to update the database 
        def update(database: list):

            # appends the object to the database
            database.append(data)

            # writes to the database
            self._storage.write(database)

        self._update_database(update)

    def _update_database(self, updater):
        """
        Updates the database by using a generic nested function
        That is passed through. 
        """

        # Reads the full raw database
        database = self._storage.read()

        # If the file is empty it returns an empty list instead of breaking the database
        if database is None:
            database = []

        # calls the nested update function
        updater(database)


    @property
    def storage(self) -> Storage:

        return self._storage


    def close(self):
        """
        Properly closes the database and makes sure
        the file handle is closed
        """

        if self._open:
            self.storage.close()