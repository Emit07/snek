
import unittest

from snek import Snek

class Test_Cache(unittest.TestCase):

	def setUp(self):
		self.db = Snek("test_database.json")
		self.db.clear_db()


	def tearDown(self):
		self.db.clear_db()
		self.db.close()


	def test_insert_return_id(self):
		
		self.db.clear_db()

		self.assertEqual(self.db.insert({"int": 0, "str": "Hello, world!"}), 0)
		self.assertEqual(self.db.insert({"name": "Don Vito Coreleone", "age": 63}), 1)
		self.assertEqual(self.db.insert({"list": [0,1,2,3,4,5]}), 2)


	def test_insert(self):

		self.db.clear_db()

		insert_objects=[{"Name": "Herbie Mann", "age": 73},
						{"Name": "Don Vito Corleone", "age": 53},
						{"_id": 1234, "market_list": ["Eggs", "Hot Sauce", "Garlic"]},
						{"Person": {"age": 31, "Class": None}}]

		for obj in insert_objects:
			self.db.insert(obj)

		database = self.db.storage.read()

		self.assertEqual(database[0], insert_objects[0])
		self.assertEqual(database[1], insert_objects[1])
		self.assertEqual(database[2], insert_objects[2])
		self.assertEqual(database[3], insert_objects[3])


	def test_get_id(self):

		self.db.clear_db()

		insert_objects=[{"Name": "Herbie Mann", "age": 73, "Instrument": "flute"},
						{"Name": "Don Vito Corleone", "age": 53},
						{"Name": "Gianni", "age": 41},
						{"Name": "Che Guevera", "age": 38},
						{"_id": 1234, "market_list": ["Eggs", "Hot Sauce", "Garlic"]},
						{"Person": {"age": 31, "Class": None}}]

		for obj in insert_objects:
			self.db.insert(obj)

		self.assertEqual(self.db.get(doc_id=0), insert_objects[0])
		self.assertEqual(self.db.get(doc_id=1), insert_objects[1])
		self.assertEqual(self.db.get(doc_id=2), insert_objects[2])
		self.assertEqual(self.db.get(doc_id=3), insert_objects[3])
		self.assertEqual(self.db.get(doc_id=4), insert_objects[4])
		self.assertEqual(self.db.get(doc_id=5), insert_objects[5])


	def test_key(self):

		self.db.clear_db()

		insert_objects=[{"Name": "Herbie Mann", "age": 73, "Instrument": "flute"},
						{"Name": "Don Vito Corleone", "age": 53},
						{"Name": "Gianni", "age": 41},
						{"Name": "Che Guevera", "age": 38},
						{"_id": 1234, "market_list": ["Eggs", "Hot Sauce", "Garlic"]},
						{"Person": {"age": 31, "Class": None}}]

		for obj in insert_objects:
			self.db.insert(obj)

		self.assertEqual(self.db.key("Name"), [insert_objects[0], insert_objects[1], insert_objects[2], insert_objects[3]])
		self.assertEqual(self.db.key("_id"), [insert_objects[4]])
		self.assertEqual(self.db.key("Person"), [insert_objects[5]])