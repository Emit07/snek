
import os
import json

class Storage:

_dir = "data/"

def insert(
    self,
    value=None,
):
    try:
        raw_json = json.load(open(f"{self.DIR}/{name}.json"))
        raw_json[container] = value
        with open(_dir, "w+") as f:
            f.write(json.dumps(raw_json))
            f.close()
    except Exception as e:
        print(e)
    
def query(
    self,
    name,
    container
):
    try:
        raw_json = json.load(open(f"{self.DIR}/{name}.json"))
        return raw_json[container]
    except Exception as e:
        print(e)