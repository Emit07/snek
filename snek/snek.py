""" 
Main module of snek
"""

import os
import json
import storage

class Snek():

    

    def __repr__(self):

        return '<{}>'.format(storage._dir)

    def __init__(self, _dir):
        storage._dir = _dir

    def __len__(self):

        return 0