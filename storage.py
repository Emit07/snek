
import os
import json

def insert(
    self,
    name,
    container,
    value=None,
):
    Value_None = Handler.check_if_none(value)
    if Value_None["passed"]:
        try:
            raw_json = json.load(open(f"{self.DIR}/{name}.json"))
            raw_json[container] = value
            with open(f"{self.DIR}/{name}.json", "w+") as f:
                f.write(json.dumps(raw_json))
                f.close()
        except Exception as e:
            print(e)
    else:
        print(Value_None["reason"])
    
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