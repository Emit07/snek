<div align="center">
	<img src="https://img.shields.io/badge/version-v0.0.1-brightgreen">
	<img src="https://img.shields.io/badge/python-3.5%2B-brightgreen">
	<img src="https://img.shields.io/github/license/emit07/snek">
	<img src="https://shields.io/github/stars/emit07/snek?style=social"> 
</div>


<div align="center">
	<img width="200" height="200" style="margin: 20px" src="https://raw.githubusercontent.com/Emit07/snek/master/logo/snek.png">
</div>	

<h1 align="center">
	SNEK
</h1>

Snek is a lightweight local nosql document oriented database which allows the user to store json data locally. Snek is meant to be readable, easy to use, and somewhat quick. A lot of inspiration comes from [TinyDB](https://github.com/msiemens/tinydb), this project would not be possible without learning from TinyDB. Snek was not developed to be used as database for a fortune 500 company or to hold every facebook account, instead it was developed for use in middle and small scale projects. My idea behind creating this was to create a small database that could be used without a big setup or fuss and also still be usefull to what I need it for. I like the idea of using something I created for projects. Another driving principle is learning from a tool. Feel free to use and improve.

### Getting Started

First off, you need to install Snek you need to have pip installed and have python running at version 3.5 minimum. You can always run Snek through source by cloning this repo. To install Snek through pip simply type whats below.

```
pip install SnekDB
```

Once you have Snek installed, set up a basic database an insert your first Document.

```python
from snek import Snek

db = Snek("test_database.json")
db.insert({"Name": "Don Vito Coreleone", "age": 63})
```

You can try to use Queries to find specific elements.

```python
from snek import Snek, Query

db = Snek("test_database.json")
db.insert({"Name": "Don Vito Coreleone", "age": 63})
db.insert({"Name": "Che Guevara", "age": 39})

query = Query()

result = db.get(query.age == 39)
```

You can also try using a read/write cache with your database. 

```python
from snek import Snek, Cache, Storage

db = Snek("test_database.json", storage=Cache(Storage))
db.insert({"Name": "John Coltrane", "age": 46})

result = db.all()
```

### TODOS

* [x] Get read/write cache working
* [ ] Implement query cache, queries can be slow (Working on this)

### Documentation will be coming soon