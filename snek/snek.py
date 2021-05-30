
""" 
Main module of snek. Handles the setup and configuration of the database
"""

from .storage import Storage
from .query import Query

from typing import Optional


class Document(dict):

    def __init__(self, value: dict, doc_id: int):

        self.value = value
        self.id = doc_id


    def __repr__(self):

        return "{}({})".format(type(self).__name__, self.id)


class Snek:

    def __init__(self, *args, **kwargs):
        """
        Initiates the snek database
        """

        # Creates a storage object to interact with the database file
        self._storage = Storage(*args, **kwargs)

        self._open = True
        self._id = None


    def insert(self, data: dict) -> int:
        """
        Inserts a single object into the database.
        TODO return the inserted object ID
        """

        # Returns an error if the object is not a dictionary
        if not isinstance(data, dict):
            # TODO rewrite a better error message
            raise ValueError("Value passed through is not a dictionary")

        _id = self._generate_id()

        # Create a function to update the database 
        def update(database: list):

            # appends the object to the database
            database.append(data)


        self._update_database(update)

        return _id


    def update(
        self, 
        data: dict, 
        cond: Optional[Query] = None, 
        doc_id: Optional[int] = None
    ) -> Document:

        # UNTESTED, STILL IN PROGRESS 

        if doc_id is not None:
            
            def update(database: list):

                database[doc_id] = data


        elif cond is not None:

            for doc in database:
                if cond(doc):
                    database[doc_id] = data


    def remove(self, doc_id: int) -> None:
        """
        Deletes an object based on its id
        """

        # Returns an error if the object is not an int
        if not isinstance(doc_id, int):
            # TODO rewrite a better error message
            raise ValueError("id is not int")

        def update(database: list):

            # Checks if the id exists, if not return an error
            if len(database)-1 >= doc_id:

                # Removes the document with the id
                database.pop(doc_id)

            else:

                # TODO Rewrite a better error message
                raise IndexError("Id does not exists")

        self._update_database(update)


    def search(self, cond: Query) -> list:
        """
        This will return an object, this is mainly for read purposes    
        """

        database = self._storage.read()

        # Checks if the condition matches the document
        objects = [Document(doc, index) for index, doc in enumerate(database) if cond(doc)]

        return objects


    def id(self, cond: Query):
        """
        Returns ID that matches query condition 
        """

        database = self._storage.read()

        ids = [index for index, doc in enumerate(database) if cond(doc)]

        return ids


    def key(self, key_name) -> dict:
        """
        Will return an object if it has the specified key
        """

        database = self._storage.read()

        objects = [doc for doc in database if key_name in doc]

        return objects


    def get(
        self, 
        cond: Optional[Query] = None,
        doc_id: Optional[int] = None 
    ) -> Optional[Document]:
        """
        Returns an object by the id
        TODO add id check (out of boudns)
        """

        database = self._storage.read()

        if doc_id is not None:

            return Document(database[doc_id], doc_id)


        elif cond is not None:

            for index, doc in enumerate(database):
                
                if cond(doc):
                    return Document(doc, index)

            return None

        raise RuntimeError("You have to pass an object id or a query")


    def clear_db(self) -> None:
        """
        Completely clears the database and resets the id,
        mostly written for the tests

        WARNING THIS ACTION CANNOT BE REVERSED
        """

        self._storage.write([])

        self._id = None


    def _generate_id(self) -> int:
        """
        If a new object needs to be inserted an ID will be generated here
        """

        # If id is not empty continue adding to it
        if self._id is not None:
            self._id += 1

            return self._id

        database = self._storage.read()

        # If the database is empty init the id
        if not database:
            self._id = 0

            return self._id

        # Else return the length of the database as the new id
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
        """
        This returns the storage handle that is used to interact with the file,
        It is not recomended to use the handle for reading and writing because
        it might interfere with the database
        """

        return self._storage


    def close(self):
        """
        Properly closes the database and makes sure
        the file handle is closed
        """

        if self._open:
            self.storage.close()
