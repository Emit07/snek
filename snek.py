""" 
Ultra lightweight local python database using json

feel free to make better!!!
"""

import os
import json

from error_handeler import Handler

class snek():

    VERSION = "0.0.1"
    INFO = {} # TODO CONFIGURE INFO {"version": "0.0.1", "Databases": {}, "stats": {"writes": 0, "reads": 0, "databases": 0}}
    DIR = "data"

    def directory(self): return self.DIR
    def set_directory(self, directory): self.DIR = directory

    # Core Functions

    def install(self):
        boiler_plate = {"version": self.VERSION, "Databases": {}, "stats": {"writes": 0, "reads": 0, "databases": 0}}

        try:
            os.mkdir(self.DIR)
            with open(f"{self.DIR}/info.json", "w+") as f:
                f.write(json.dumps(boiler_plate))
                f.close()
        except Exception as e:
            print(e)

    def uninstall(self):
        print(f"""
        WARNING

        THIS WILL DELETE {self.DIR} DIRECTORY
        THIS ACTION CANNOT BE UNDONE PROCEED WITH CAUTION

        continue? (y/n)
        """)
        answ = input("> ")
        if answ.upper() in ["Y", "YES"]: shutil.rmtree(self.DIR)
        else: pass # TODO HANDLE ELSE

    def info(self):

        info_dir = f"{self.DIR}/info.json"

        if os.path.exists(self.DIR): INFO = json.load(open(info_dir))
        else: self.install() 

        return self.INFO
    
    def create_db(self, name):
        try:
            with open(f"{self.DIR}/{name}.json", "w+") as f:
                f.write(json.dumps({"default": {}}))
                f.close()
        except Exception as e:
            print(e)

    def remove_db(self, name):
        try:
            os.remove(f"{self.DIR}/{name}.json")
        except Exception as e:
            print(e)
    
    def __init__(self):
        pass # print(self.read_container("test", "default"))