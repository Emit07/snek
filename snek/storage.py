
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
        with File(config.__dir__, "w+") as f:
            f.write(data)
            f.close()

    def insert(self, value : dict):
        pulled = self.read()
        pulled.append(value)
        self.write(pulled)

    def remove(self, value):
        
        pulled = self.read()
        for index, item in enumerate(pulled):
            if value.items() <= item.items(): del pulled[index]

        self.write(pulled)
    
    def find(self, value : dict):
        # TODO does not run fast fix that
        pulled = self.read()
        if isinstance(value, dict):
            for index, item in enumerate(pulled):
                res = value.items() <= item.items() 
                if res: return item
    
    def update(self, value : dict):
        pass

    def exists(self, value : dict):

        pulled = self.read()
        for index, item in enumerate(pulled):
            return value.items() <= item.items() 
    
    def initdb(self):
        os.mkdir(config.__dir__)
        self.write([])

    def key(self, value):

        pulled = self.read()
        return pulled[value] if value in pulled else None