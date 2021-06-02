

class Middleware:
		
	def __init__(self, storage_class):
		"""
		Middleware class to hold the storage object. Middlewares are able to tap 
		into the storage object allowing to log, cache, and do other things that 
		require interaction with the Storage object
		"""

		self._storage_class = storage_class
		self._storage = None


	def __call__(self, *args, **kwargs):
		"""
		When this class is called it creates a storage object
		"""

		self._storage = self._storage_class(*args, **kwargs)

		return self


class Cache(Middleware):


	def __init__(self, storage_class, modification_limit: int = 50):
		"""
		This is a cache that is meant to speed up the database by saving
		the data in memory and not reading/writing everytime that an
		operation needs to be performed.
		"""

		super().__init__(storage_class)

		# Where the memory will go
		self.memory = []

		# Keeps track of the cache modifcations and will write them if 
		# it exceeds a threshold
		self._cache_modifications = 0
		self._modification_limit = modification_limit


	def read(self):
		# Function for read from memory

		# If the memory is empty it will read from the database to
		# initialize it
		if self.memory == []:
			self.memory = self._storage.read()

		return self.memory


	def write(self, data: dict):

		# It will apply the data to the memory
		self.memory = data
		# Adds to cache modifications
		self._cache_modifications += 1

		# If the cache modifications exceed the limit it writes the the file
		if self._cache_modifications >= self._modification_limit:
			self.apply()


	def apply(self):
		# Applies the memory to the file.
		self._storage.write(self.memory)

		self._cache_modifications = 0


	def close(self):
		# Writes any unwritten changes to the database
		self.apply()

		# Closes the file handle properly
		self._storage.close()