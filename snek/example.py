from snek import Snek

snek = Snek("database.json")

results = snek.find("name")
print(results)