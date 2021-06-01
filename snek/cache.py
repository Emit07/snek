

class Middleware:
		
	def __init__(self, storage_class):

		self._storage_class = storage_class
		self._storage = None


	def __call__(self, *args, **kwargs):

		self._storage = self._storage_class(*args, **kwargs)

		return self


class Cache(Middleware):


	def __init__(self, storage_class):

		super().__init__(storage_class)

		self.memory = []

		self._cache_modifications = 0
		self._modification_limit = 50


	def read(self):
		if self.memory == []:
			self.memory = self._storage.read()

		return self.memory


	def write(self, data: dict):

		self.memory = data
		self._cache_modifications += 1

		if self._cache_modifications >= self._modification_limit:
			self.apply()


	def apply(self):

		self._storage.write(self.memory)

		self._cache_modifications = 0


	def close(self):

		self.apply()

		self._storage.close()