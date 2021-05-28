from snek.snek import Snek
from snek.query import Query
from snek.storage import Storage

import snek.query as query

class Tests:

	def __init__(self):
		# Create the instance
		self.db = Snek(path="test_database.json", mode="w+", create_dir=True)

		# Call the tests

		print("TESTING\n" + "-" * 15)

		self.test_insert(0)
		self.test_insert_id(1)
		self.test_get(2)
		self.test_key(3)
		self.test_search(4)
		self.test_id(5)

		# Do the database teardown

		self.db.clear_db()
		self.db.close()

	def test_insert_id(self, test_number):

		self.db.clear_db()

		assert self.db.insert({"age": 21, "Name": "Marco"}) == 0
		assert self.db.insert({"int": 100, "Math": 3*8**3/2}) == 1
		assert self.db.insert({"list": [1,2,3,4,5]}) == 2

		print(f"{test_number} PASSED TEST INSERT ID")


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

		print(f"{test_number} PASSED TEST INSERT")


	def test_get(self, test_number):

		self.db.clear_db()

		insert_objects=[{"Name": "Herbie Mann", "age": 73},
						{"Name": "Don Vito Corleone", "age": 53},
						{"_id": 1234, "market_list": ["Eggs", "Hot Sauce", "Garlic"]},
						{"Person": {"age": 31, "Class": None}}]

		ids = []

		for obj in insert_objects:
			new_id = self.db.insert(obj)

			ids.append(new_id)

		for _id in ids:
			assert self.db.get(_id) == insert_objects[_id]

		print(f"{test_number} PASSED TEST GET")


	def test_key(self, test_number):

		self.db.clear_db()

		insert_objects=[{"Name": "Herbie Mann", "age": 73},
						{"Name": "Don Vito Corleone", "age": 53},
						{"_id": 1234, "market_list": ["Eggs", "Hot Sauce", "Garlic"]},
						{"Person": {"age": 31, "Class": None}},
						{"a": 2}]

		ids = []

		for obj in insert_objects:
			new_id = self.db.insert(obj)


		assert self.db.key("Person") == [insert_objects[3]]
		assert self.db.key("Does not exist") != 0

		print(f"{test_number} PASSED TEST KEY")


	def test_search(self, test_number):

		self.db.clear_db()

		insert_objects=[{"Name": "Herbie Mann", "age": 73},
						{"Name": "Don Vito Corleone", "age": 53},
						{"Name": "Gianni", "age": 41},
						{"Name": "Che Guevera", "age": 38},
						{"_id": 1234, "market_list": ["Eggs", "Hot Sauce", "Garlic"]},
						{"Person": {"age": 31, "Class": None}},
						{"a": 2}]

		ids = []

		for obj in insert_objects:
			new_id = self.db.insert(obj)

		User = Query()

		assert self.db.search(User.age == 73) == [insert_objects[0]]
		assert self.db.search(User._id != 1) == [insert_objects[4]]
		assert self.db.search(User.age < 40) == [insert_objects[3]]
		assert self.db.search(User.age > 48) == [insert_objects[0], insert_objects[1]]
		assert self.db.search(User.Name == "Herbie Mann") == [insert_objects[0]]
		assert self.db.search(User.Person == {"age": 31, "Class": None}) == [insert_objects[5]]

		print(f"{test_number} PASSED TEST SEARCH")


	def test_id(self, test_number):

		self.db.clear_db()

		insert_objects=[{"Name": "Herbie Mann", "age": 73},
						{"Name": "Don Vito Corleone", "age": 53},
						{"_id": 1234, "market_list": ["Eggs", "Hot Sauce", "Garlic"]},
						{"Person": {"age": 31, "Class": None}},
						{"a": 2}]

		for obj in insert_objects:
			new_id = self.db.insert(obj)


		User = Query()

		ids = self.db.id(User.Name == "Herbie Mann")


if __name__ == "__main__":
	Tests()