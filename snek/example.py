import os
import json

from snek import Snek


DIR = "database.json"
snek = Snek(DIR)

def clear():
    global DIR
    os.rmdir(DIR)

def test_write(value):
    snek.insert(value)

if __name__ == "__main__":
    # test_write({"name": "John Smith"})
    print(snek.find({"name": "John asdsSmith"}))