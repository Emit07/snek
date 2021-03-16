import unittest
from snek.snek import Snek

class TestSnek(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        print("SETUP")
        self.db = Snek("database.json")
        self.hasfound = False
        

    def test_find(self):
        print("FIND")
        self.assertEqual(self.db.find({"name": "Giovanni Esposito"}), {"name": "Giovanni Esposito", "age": 17, "classes": ["Math", "Science", "Calculus"]})
        self.assertEqual(self.db.find("Jane"), None)
        self.assertEqual(self.db.find({"name": "Johnny B. Good"}), None)
        self.hasfound = True

    def test_insert(self):
        print("INSERT")
        self.db.insert({"new inserted": True})
        if self.hasfound:
            self.assertEqual(self.db.find({"new inserted": True}), {"new inserted": True})
            self.assertEqual(self.db.find({"this exists": False}), None)
            self.assertEqual(self.db.find({12345}), None)
    
    def test_remove(self):
        print("REMOVE")
        self.assertEqual(self.db.find({"new inserted": True}), {"new inserted": True})
        self.db.remove({"new inserted": True})
        self.assertEqual(self.db.find({"new inserted": True}), None)

    def test_key(self):
        print("KEY")
        

if __name__ == "__main__":
    unittest.main()