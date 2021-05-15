from snek.snek import Snek
from snek.storage import Storage

if __name__ == "__main__":

    db = Snek(path="test_database.json", mode="w+", create_dir=True)
    print(db.insert({"Test": 2}))