from snek.snek import Snek
import json

db = Snek("database.json")

pulled = json.load(open("database.json"))

value = {"name": "Alessandro De Leo"}

db.remove(value)

# namein = input("name: ")
# agein = int(input("age: "))
# classesin = list(input("classes: ").split(' '))

# data = {
#     "name": namein,
#     "age": agein,
#     "classes": classesin
# }

# db.insert(data)
