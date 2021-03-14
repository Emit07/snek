
import os
import json
import snek.config as config

class File:

    def __init__(self, filedir, operation):
        self.file = open(filedir, operation)
    
    def __enter__(self):
        return self.file
    
    def __exit__(self, type, value, traceback):
        self.file.close()
        # TODO create exception handler

class Storage(object):

    def read(self): 
        
        """
        Reads from json database file
        TODO if you properly cose the
        file it results in ugly code
        TODO properly close the file
        without having ugly function
        """

        return json.load(open(config.__dir__))

    def write(self, value):
        data = json.dumps(value, ensure_ascii=False, indent=4)
        with File(config.__dir__, "w+") as f:
            f.write(data)
            f.close()

    def insert(self, value : dict):
        try:
            pulled = self.read()
            pulled.update(value)
            self.write(pulled)
        except Exception as e:
            raise e

    def remove(self, value):
        
        pulled = self.read()
        del pulled[value]
        self.write(pulled)
    
    def find(self, value):
        # TODO make this work, mongodb style find
        pass

    def exists(self, value : dict):

        pulled = self.read()
        return all(item in pulled.items() for item in value.items())

    def key(self, value):

        pulled = self.read()
        return pulled[value] if value in pulled else None