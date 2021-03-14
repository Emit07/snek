import unittest
import json
import os
from snek.snek import Snek

class TestSnek(unittest.TestCase):

    _dir = "database.json"
    _value = {"name": "John Smith"}
    with open(_dir, "w+") as f:
        f.write(json.dumps({}))
        f.close()
    db = Snek(_dir)

    def test_insert(self):
        self.db.insert(self._value)
        self.assertEqual(db.read(), self._value)

if __name__ == "__main__":
    unittest.main()