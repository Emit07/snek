
import os
import json 

class File:

    def __init__(self, filedir, operation):
        self.file = open(filedir, operation)
    
    def __enter__(self):
        print("ENTER")
        return self.file
    
    def __exit__(self, type, value, traceback):
        print("EXIT")
        self.file.close()
        # TODO create exception handler

class Storage(object):

    def read(self): 
        return json.load(open(config._dir))

    def write(self, value):
        data = json.dumps(value, ensure_ascii=False, indent=4)
        with File(config._dir, "w+") as f: f.write(data)

    def insert(self, value : dict):
        
        pulled = json.load(open(config._dir))
        pulled.update(value)
        self.write(pulled)
        
    def remove(self, value):
        
        pulled = self.read()
        del pulled[value]
        self.write(pulled)

    def find(self, value : dict):

        pulled = self.read()
        return 