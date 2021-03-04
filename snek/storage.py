
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
        
    def remove(self, value):
        pulled = self.read()
        del pulled[value]
        self.write(pulled)

    def key_exists(self, value):
        pulled = self.read()
        return True if value in pulled else False
    
    def exists(self, value):
        pulled = self.read()
        valuelist = list(value)
        key = valuelist[0] 
        key_value = value[valuelist[0]]
        if key in pulled:
            if pulled[key] == key_value:
                return True
            return False
        else:
            return False

    def find(self, value : str):
        pulled = self.read()
        return pulled[value]