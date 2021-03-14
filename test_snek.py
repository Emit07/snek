import unittest
import json
import os
from snek.snek import Snek

class TestSnek(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self._dir = "database.json"
        self._value = {"name": "John Smith"}
        with open(self._dir, "w+") as f:
            f.write(json.dumps({}))
            f.close()
        self.db = Snek(self._dir)

    def test_insert(self):
        self.db.insert(self._value)
        self.assertEqual(self.db.read(), self._value)
    
    def test_key(self):
        
        print("\n\n\n", self.db.key("notexisting"), "\n\n\n")
        
        self.assertEqual(self._value[list(self._value)[0]], self.db.key(list(self._value)[0])) 
        self.assertEqual("notexisting", "key does not exist")

if __name__ == "__main__":
    unittest.main()

