
import os
import json

class Storage:

    _dir = ""

    def __init__(self, _dir):
        self._dir = _dir

    def read(self):
        return json.load(open(self._dir))

    def write(self, value):
        with open(self._dir, "w+") as f:
            f.write(json.dumps(value))
            f.close()

    def insert(self, value : dict):
        pulled = json.load(open(self._dir))
        pulled.update(value)
        self.write(pulled)
        
    def remove(self, value : str):
        pulled = self.read()
        del pulled[value]
        self.write(pulled)

    def query(self, value):
        pulled = self.read()
        pulledlist = list(value) 
        return pulledlist[0]
        
    def find(self, value : str):
        pulled = self.read()
        return pulled[value]