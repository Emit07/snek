import unittest
import json
import os
from snek.snek import Snek

class TestSnek(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self._dir = "database.json"
        self._value = {"_id": 123456789}
        with open(self._dir, "w+") as f:
            f.write(json.dumps([]))
            f.close()
        self.db = Snek(self._dir)

    def test_insert(self):
        self.db.insert(self._value)
        # self.assertEqual(self.db.read(), self._value)
    
    def test_key(self):
        pass
        # self.assertEqual(self.db.key(list(self._value)[0]), "John Smith") 
        # self.assertEqual(self.db.key("notexisting"), None)

if __name__ == "__main__":
    unittest.main()

