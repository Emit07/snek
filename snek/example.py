from snek import Snek

snek = Snek("database.json")

# print(snek)

results = snek.write({"class": "history"})
print(results)