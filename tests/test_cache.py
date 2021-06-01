
import unittest

from snek import Snek
from snek.storage import Storage
from snek.cache import Cache

class Test_Cache(unittest.TestCase):

	def setUp(self):
		self.db = Snek("test_database.json", storage=Cache(Storage))
		self.db.clear_db()


	def tearDown(self):
		self.db.clear_db()
		self.db.close()


	def test_read(self):
		
		self.db.clear_db()

		insert_objects=[{"Name": "Herbie Mann", "age": 73, "Instrument": "flute"},
						{"Name": "Don Vito Corleone", "age": 53},
						{"Name": "Gianni", "age": 41},
						{"Name": "Che Guevera", "age": 38},
						{"_id": 1234, "market_list": ["Eggs", "Hot Sauce", "Garlic"]},
						{"Person": {"age": 31, "Class": None}}]

		for obj in insert_objects:
			self.db.insert(obj)

		self.assertEqual(self.db.all(), insert_objects)


	def test_write(self):

		self.db.clear_db()

		insert_objects=[{"Name": "Herbie Mann", "age": 73, "Instrument": "flute"},
						{"Name": "Don Vito Corleone", "age": 53},
						{"Name": "Gianni", "age": 41},
						{"Name": "Che Guevera", "age": 38},
						{"_id": 1234, "market_list": ["Eggs", "Hot Sauce", "Garlic"]},
						{"Person": {"age": 31, "Class": None}}]

		for obj in insert_objects:
			self.db.insert(obj)

		self.assertEqual(self.db.all(), insert_objects)
		self.db.storage.write([])
		self.assertEqual(self.db.all(), [])