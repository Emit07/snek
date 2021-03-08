
import os
import json
import config

class Storage(object):

    def read(self):
        return json.load(open(config._dir))

    def write(self, value):
        
        data = json.dumps(value, ensure_ascii=False, indent=4)
        
        with open(config._dir, "w+") as f:
            f.write(data)
            f.close()

    def insert(self, value : dict):
        
        pulled = json.load(open(config._dir))
        
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