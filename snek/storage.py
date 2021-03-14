
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
        return json.load(open(config.__dir__))

    def write(self, value):
        data = json.dumps(value, ensure_ascii=False, indent=4)
        with File(config.__dir__, "w+") as f: f.write(data)

    def insert(self, value : dict):
        try:
            pulled = json.load(open(config.__dir__))
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
        return all(pulled.get(key, None) == val for key, val in value.items())

    def key(self, value):

        pulled = self.read()
        return pulled[value]