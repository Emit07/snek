
import os
import json

class Cache:

    def __init__(self, value):
        self.cache = value

    def update(self, value):
        self.cache = value

    def retrive(self):
        return self.cache