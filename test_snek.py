from snek.snek import Snek
from snek.query import Query
from snek.storage import Storage
from snek.cache import Cache

import time

class Tests:

	def __init__(self):
		# Create the instance
		self.db = Snek("test_database.json")

		# Call the tests

		print("TESTING\n" + "-" * 15)

		starttime = time.time()

		self.test_insert(0)
		self.test_insert_id(1)
		self.test_get_id(2)
		self.test_get_query(3)
		self.test_key(4)
		self.test_search(5)
		self.test_id(6)
		self.test_update_id(7)

		print("#" * 15 + "\n" + "Time: " + str(round(time.time() - starttime, 4)))

		# Do the database teardown

		self.db.clear_db()
		self.db.close()

	def test_insert_id(self, test_number):

		self.db.clear_db()

		test_starttime = time.time()

		assert self.db.insert({"age": 21, "Name": "Marco"}) == 0
		assert self.db.insert({"int": 100, "Math": 3*8**3/2}) == 1
		assert self.db.insert({"list": [1,2,3,4,5]}) == 2

		print(f"{test_number} - {round(time.time() - test_starttime, 4)}: PASSED TEST INSERT ID")


	def test_insert(self, test_number):

		self.db.clear_db()

		test_starttime = time.time()

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

		print(f"{test_number} - {round(time.time() - test_starttime, 4)}: PASSED TEST INSERT")


	def test_get_id(self, test_number):

		self.db.clear_db()

		test_starttime = time.time()

		insert_objects=[{"Name": "Herbie Mann", "age": 73},
						{"Name": "Don Vito Corleone", "age": 53},
						{"_id": 1234, "market_list": ["Eggs", "Hot Sauce", "Garlic"]},
						{"Person": {"age": 31, "Class": None}}]

		ids = []

		for obj in insert_objects:
			new_id = self.db.insert(obj)

			ids.append(new_id)

		for _id in ids:
			id_doc = self.db.get(doc_id=_id)
			assert id_doc == insert_objects[_id]
			assert id_doc.id == _id

		print(f"{test_number} - {round(time.time() - test_starttime, 4)}: PASSED TEST GET ID")


	def test_get_query(self, test_number):

		self.db.clear_db()

		test_starttime = time.time()

		insert_objects=[{"Name": "Herbie Mann", "age": 73, "Instrument": "flute"},
						{"Name": "Don Vito Corleone", "age": 53},
						{"Name": "Gianni", "age": 41},
						{"Name": "Che Guevera", "age": 38},
						{"_id": 1234, "market_list": ["Eggs", "Hot Sauce", "Garlic"]},
						{"Person": {"age": 31, "Class": None}},
						{"a": 2}]

		for obj in insert_objects:
			new_id = self.db.insert(obj)

		User = Query()

		assert self.db.get(cond=User.age == 73) == insert_objects[0]
		assert self.db.get(cond=User._id != 1) == insert_objects[4]
		assert self.db.get(cond=User.age < 40) == insert_objects[3]
		assert self.db.get(cond=User.age > 48) == insert_objects[0], insert_objects[1]
		assert self.db.get(cond=User.Name == "Herbie Mann") == insert_objects[0]

		print(f"{test_number} - {round(time.time() - test_starttime, 4)}: PASSED TEST GET QUERY")


	def test_key(self, test_number):

		self.db.clear_db()

		test_starttime = time.time()

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

		print(f"{test_number} - {round(time.time() - test_starttime, 4)}: PASSED TEST KEY")


	def test_search(self, test_number):

		self.db.clear_db()

		test_starttime = time.time()

		insert_objects=[{"Name": "Herbie Mann", "age": 73, "Instrument": "flute"},
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

		assert self.db.search(User.age == 73)[0] == insert_objects[0]
		assert self.db.search(User._id != 1)[0] == insert_objects[4]
		assert self.db.search(User.age < 40)[0] == insert_objects[3]
		assert self.db.search(User.age > 48)[0] == insert_objects[0], insert_objects[1]
		assert self.db.search(User.Name == "Herbie Mann")[0] == insert_objects[0]
		assert self.db.search(User.Person == {"age": 31, "Class": None})[0] == insert_objects[5]

		print(f"{test_number} - {round(time.time() - test_starttime, 4)}: PASSED TEST SEARCH")


	def test_id(self, test_number):

		self.db.clear_db()

		test_starttime = time.time()

		insert_objects=[{"Name": "Herbie Mann", "age": 73},
						{"Name": "Don Vito Corleone", "age": 53},
						{"_id": 1234, "market_list": ["Eggs", "Hot Sauce", "Garlic"]},
						{"Person": {"age": 31, "Class": None}},
						{"a": 2}]

		for obj in insert_objects:
			new_id = self.db.insert(obj)


		User = Query()

		ids = self.db.id(User.Name == "Herbie Mann")

		print(f"{test_number} - {round(time.time() - test_starttime, 4)}: PASSED TEST ID")


	def test_update_id(self, test_number):

		self.db.clear_db()

		test_starttime = time.time()

		insert_objects=[{"Name": "Herbie Mann", "age": 73, "Instrument": "flute"},
						{"Name": "Don Vito Corleone", "age": 53},
						{"Name": "Gianni", "age": 41},
						{"Name": "Che Guevera", "age": 38},
						{"_id": 1234, "market_list": ["Eggs", "Hot Sauce", "Garlic"]},
						{"Person": {"age": 31, "Class": None}},
						{"a": 2}]

		for obj in insert_objects:
			new_id = self.db.insert(obj)

		assert self.db.get(doc_id=0) == insert_objects[0]
		self.db.update({"age": 50}, doc_id=0)
		assert self.db.get(doc_id=0) == {"age": 50}

		print(f"{test_number} - {round(time.time() - test_starttime, 4)}:PASSED UPDATE ID")


if __name__ == "__main__":
	Tests()