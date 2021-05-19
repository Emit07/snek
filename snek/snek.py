
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
        self._id = None

    def insert(self, data: dict) -> None:
        """
        Inserts a single object into the database.
        TODO return the inserted object ID
        """

        # Returns an error if the object is not a dictionary
        if not isinstance(data, dict):
            # TODO rewrite a better error message
            raise ValueError("Data is not dict")


        # Create a function to update the database 
        def update(database: list):

            # appends the object to the database
            database.append(data)


        self._update_database(update)


    def remove(self, object_id: int) -> None:
        """
        Deletes an object based on its id
        """

        # Returns an error if the object is not an int
        if not isinstance(object_id, int):
            # TODO rewrite a better error message
            raise ValueError("id is not int")

        def update(database: list):

            # Checks if the id exists, if not return an error
            if len(database)-1 >= object_id:

                # Removes the document with the id
                database.pop(object_id)

            else:

                # TODO Rewrite a better error message
                raise IndexError("Id does not exists")

        self._update_database(update)


    def _generate_id(self) -> int:
        """
        If a new object needs to be inserted an ID will be generated here
        """

        if self._id is not None:
            _id = self._id
            self._id += 1

            return _id

        database = self._storage.read()

        self._id = len(database)

        return self._id

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

        self._storage.write(database)

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
