import unittest
from snek.snek import Snek

class TestSnek(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        print("SETUP")
        self.db = Snek("database.json")

    def test_insert(self):
        print("INSERT")

    def test_remove(self):
        print("REMOVE")

    def test_find(self):
        print("FIND")
        self.assertEqual(self.db.find({"name": "Giovanni Esposito"}), {"name": "Giovanni Esposito", "age": 17, "classes": ["Math", "Science", "Calculus"]})
        self.assertEqual(self.db.find({"name": "Johnny B. Good"}), None)
        self.assertEqual(self.db.find("Jane"), None)

    def test_key(self):
        print("KEY")
        

if __name__ == "__main__":
    unittest.main()