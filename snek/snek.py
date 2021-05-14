
""" 
Main module of snek. Handles the setup and configuration of the database
"""

import os
import json

from .storage import Storage
from .document import Document

class Snek:

    def __init__(self, path: str, mode="r+", create_dir=False):

        self._storage = Storage(path, mode, create_dir)
        self._documents = []

    def create_document(self):

        document = Document(self._storage)
        self._documents.append(document)

        return document

    def remove_document(self):

        pass

    def __enter__(self):

        return self

    def __exit__(self):

        if self._open:
            self.storage.close()