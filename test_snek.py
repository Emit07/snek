from snek.snek import Snek

from snek.storage import Storage

class TestSnek:

    def test_find(self):
        print("TESTING FIND")

        db_find_name = (
            self.db.find({"name": "Don Vito Corleone"}),
            [{"name": "Don Vito Corleone", "age": 62}]
        )
        db_find_age = (
            self.db.find({"age": 59}),
            [{"name": "Michael", "age": 59}]
        )
        db_find_empty = (
            self.db.find({"name": "Paulie"}), 
            []
        )

        find_tests = [db_find_name, db_find_age, db_find_empty]

        for index, test in enumerate(find_tests):
            assert test[0] == test[1], f"FIND TEST {index+1}/{len(find_tests)} - ERROR : SHOULD RESULT AS {test}"
            print(f"FIND TEST {index+1}/{len(find_tests)} - PASSED")

        print("FIND TESTS PASSED")

    def __init__(self):
        print("SETUP")
        self.db = Snek("test_database.json")
        
        # TESTS

        self.test_find()
        # self.test_insert()
        # self.test_remove()
        # self.test_key()

if __name__ == "__main__":
    # TestSnek()

    stor = Snek(path="test_database.json", mode="w+", create_files=True)
