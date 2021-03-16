from snek.snek import Snek
import json

db = Snek("database.json")

pulled = json.load(open("database.json"))

print(db.find({"new inserted": True}))


        # self.dbvalue1= {
        #     "name": "John Smith",
        #     "age": 27,
        #     "classes": [
        #         "America_History",
        #         "English",
        #         "Photography"
        #     ]
        # }
        # self.dbvalue2 = {
        #     "name": "Giovanni Esposito",
        #     "age": 17,
        #     "classes": [
        #         "Math",
        #         "Science",
        #         "Calculus"
        #     ]
        # }

# namein = input("name: ")
# agein = int(input("age: "))
# classesin = list(input("classes: ").split(' '))

# data = {
#     "name": namein,
#     "age": agein,
#     "classes": classesin
# }

# db.insert(data)
