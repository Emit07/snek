import os
import json


class Handle:

    def __init__(self, filedir, operation):
        self.file = open(filedir, operation)
    
    def __enter__(self):
        return self.file
    
    def __exit__(self, type, value, traceback):
        self.file.close()
        # create exception handler