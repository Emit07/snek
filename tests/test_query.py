
import unittest

from snek import Snek
from snek.query import Query


class Test_Query(unittest.TestCase):

	def setUp(self):
		self.db = Snek("test_database.json")
		self.db.clear_db()


	def tearDown(self):
		self.db.clear_db()
		self.db.close()


	def test_get(self):

		self.db.clear_db()

		insert_objects=[{"Name": "Herbie Mann", "age": 73, "Instrument": "flute"},
						{"Name": "Don Vito Corleone", "age": 53},
						{"Name": "Gianni", "age": 41},
						{"Name": "Che Guevera", "age": 38},
						{"_id": 1234, "market_list": ["Eggs", "Hot Sauce", "Garlic"]},
						{"Person": {"age": 31, "Class": None}}]

		for obj in insert_objects:
			self.db.insert(obj)

		query = Query()

		self.assertEqual(self.db.get(query.age == 41), insert_objects[2])
		self.assertEqual(self.db.get(query._id != 123), insert_objects[4])
		self.assertEqual(self.db.get(query.age < 53), insert_objects[2])

	def test_search(self):

		self.db.clear_db()

		insert_objects=[{"Name": "Herbie Mann", "age": 73, "Instrument": "flute"},
						{"Name": "Don Vito Corleone", "age": 53},
						{"Name": "Gianni", "age": 41},
						{"Name": "Che Guevera", "age": 38},
						{"_id": 1234, "market_list": ["Eggs", "Hot Sauce", "Garlic"]},
						{"Person": {"age": 31, "Class": None}}]

		for obj in insert_objects:
			self.db.insert(obj)

		query = Query()

		self.assertEqual(self.db.search(query.Name == "Herbie Mann"), [insert_objects[0]])
		self.assertEqual(self.db.search(query.age >= 41), [insert_objects[0], insert_objects[1], insert_objects[2]])
		self.assertEqual(self.db.search(query._id == 123), [])
		self.assertEqual(self.db.search(query.notexist == 0), [])
		self.assertEqual(self.db.search(query.Person == {"age": 31, "Class": None}), [insert_objects[5]])

	def test_id(self):

		self.db.clear_db()

		insert_objects=[{"Name": "Herbie Mann", "age": 73, "Instrument": "flute"},
						{"Name": "Don Vito Corleone", "age": 53},
						{"Name": "Gianni", "age": 41},
						{"Name": "Che Guevera", "age": 38},
						{"_id": 1234, "market_list": ["Eggs", "Hot Sauce", "Garlic"]},
						{"Person": {"age": 31, "Class": None}}]

		for obj in insert_objects:
			self.db.insert(obj)

		query = Query()

		self.assertEqual(self.db.id(query.Name == "Herbie Mann"), [0])
		self.assertEqual(self.db.id(query.age > 18), [0, 1, 2, 3])
		self.assertEqual(self.db.id(query.notexist == 0), [])
