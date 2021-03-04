from snek import Snek

snek = Snek("database.json")

results = snek.query({"name": "Alessandro"})
# print(results)