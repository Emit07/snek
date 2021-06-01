
""" 
Main module of snek. Handles the setup and configuration of the database
"""

from .storage import Storage
from .query import Query
from .cache import Cache

from typing import Optional, Dict, Callable, Any, Iterator


class Document(dict):

    def __init__(self, value: dict, doc_id: int):

        super().__init__(value)
        self.id = doc_id


class Snek:


    def __init__(self, *args, **kwargs):
        """
        Initiates the snek database
        """

        storage = kwargs.pop("storage", Storage)

        self._storage = storage(*args, **kwargs)

        self._open = True
        self._id = None


    def __len__(self) -> int:

        return len(self._storage.read())


    def insert(self, data: dict) -> int:
        """
        Inserts a single document into the database.
        """

        # Returns an error if the document is not a dictionary
        if not isinstance(data, dict):
            # TODO rewrite a better error message
            raise ValueError("Value passed through is not a dictionary")

        _id = self._generate_id()

        # Create a function to update the database 
        def update(database: list):

            # appends the document to the database
            database.append(data)


        self._update_database(update)

        return _id


    def update(
        self, 
        data: dict, 
        cond: Optional[Query] = None, 
        doc_id: Optional[int] = None
    ) -> Document:

        """
        Updates a document, takes in either an id or a query
        
        TODO allow appending, removing, and overwrite config
        STILL IN PROGRESS 
        """

        # If a doc_id is provided then use to doc_id to index the doc
        if doc_id is not None:
            
            def update(database: list):
                # Updates the inedx 
                database[doc_id] = data

        # If a doc_id is not provided but a condition is use the condition to index 
        elif cond is not None:

            # pulls the database to iterate over the database
            # TODO rewrite, why pull the database twice?
            iter_database = self._storage.read()
            
            # iterates over database applying query to each document
            for index, doc in enumerate(iter_database):
                if cond(doc):

                    def update(database: list):
                        # Updates the idex
                        database[index] = data

        else:

            # Raises an error if no paramteres to address the doc are passed
            raise RuntimeError("A doc_id or a cond (query) has to be provided")

        self._update_database(update) 


    def remove(self, doc_id: int) -> None:
        """
        Deletes an document based on its id
        """

        # Returns an error if the doc_id is not an int
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
        This will return an document if it matches the query   
        """

        database = self._storage.read()

        # Checks if the condition matches the document
        documents = [Document(doc, index) for index, doc in enumerate(database) if cond(doc)]

        return documents


    def get(
        self, 
        cond: Optional[Query] = None,
        doc_id: Optional[int] = None 
    ) -> Optional[Document]:
        """
        Returns an document by the id
        TODO add id check (out of bounds)
        """

        # Pulls a database to preform actions on
        database = self._storage.read()

        # If a doc_id is passed return a document object with the doc_id
        if doc_id is not None:

            return Document(database[doc_id], doc_id)


        # If there is no doc_Id and a cond is passed use that instead
        elif cond is not None:

            # Iterates over the database and checks if condition applies
            for index, doc in enumerate(database):
                
                if cond(doc):
                    return Document(doc, index)

            return None

        # Raises an error if no indexing are passed through
        raise RuntimeError("You have to pass an doc_id or a cond (query)")


    def all(self) -> list:
        """
        Returns all the documents in the database
        """

        return self._storage.read()


    def id(self, cond: Query):
        """
        Returns ID that matches query condition 
        """

        database = self._storage.read()

        ids = [index for index, doc in enumerate(database) if cond(doc)]

        return ids


    def key(self, key_name: Any) -> dict:
        """
        Will return a document if it has the specified key
        """

        database = self._storage.read()

        documents = [doc for doc in database if key_name in doc]

        return documents


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
        If a new document needs to be inserted an ID will be generated here
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
