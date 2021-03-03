
from snek import snek

if __name__ == "__main__":
    cmd = input("> ")
    snek.insert("test", cmd, {"_id": 123456})
    results = snek.query("test", cmd)
    print(results)
    