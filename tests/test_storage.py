
import unittest

from snek.storage import Storage

class TestStorage(unittest.TestCase):

	def setUp(self):
		self._storage = Storage("test_database.json", mode="w+")

	
	def tearDown(self):
		self._storage.write([])
		self._storage.close()


	def test_read_write(self):

		self._storage.write([])

		example_object1 = [{"a":0, "b":1}]
		example_object2 = [{"a": 10, "b": 20}]

		self._storage.write(example_object1)
		self.assertEqual(self._storage.read(), example_object1)
		self._storage.write(example_object2)
		self.assertEqual(self._storage.read(), example_object2)


	def test_size(self):

		self._storage.write("12345")

		self.assertEqual(self._storage.size, 7)
