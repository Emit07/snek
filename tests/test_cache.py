
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
		self.db.insert({"int": 0, "char": "a"})