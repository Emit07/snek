from snek.snek import Snek
from snek.storage import Storage

class Tests:

	def __init__(self):
		# Create the instance
		self.db = Snek(path="test_database.json", mode="w+", create_dir=True)

		# Call the tests

		print("TESTING\n" + "-" * 15)

		self.test_insert("0")
		self.test_insert_id("1")

		# Do the database teardown

		self.db.clear_db()
		self.db.close()

	def test_insert_id(self, test_number):

		self.db.clear_db()

		assert self.db.insert({"age": 21, "Name": "Marco"}) == 0
		assert self.db.insert({"int": 100, "Math": 3*8**3/2}) == 1
		assert self.db.insert({"list": [1,2,3,4,5]}) == 2

		print(f"PASSED {test_number}")

	def test_insert(self, test_number):

		self.db.clear_db()

		insert_objects=[{"Name": "Herbie Mann", "age": 73},
						{"Name": "Don Vito Corleone", "age": 53},
						{"_id": 1234, "market_list": ["Eggs", "Hot Sauce", "Garlic"]},
						{"Person": {"age": 31, "Class": None}}]

		ids = []

		for obj in insert_objects:
			new_id = self.db.insert(obj)

			ids.append(new_id)

		database = self.db.storage.read()

		for index, _id in enumerate(ids):
			assert database[_id] == insert_objects[index]

		print(f"PASSED {test_number}")

if __name__ == "__main__":
	Tests()