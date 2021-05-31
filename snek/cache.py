

class Cache:


	def __init__(self, storage, modification_limit: int = 50):
		
		print("CACHE BEING USED")

		self._storage = storage

		self.memory = []

		self._cache_modifications = 0
		self._modification_limit = modification_limit


	def read(self):
		if self.memory == []:
			self.memory = self._storage.read()

		return self.memory


	def write(self, data: dict):

		self.memory.append(data)
		self._cache_modifications += 1

		if self._cache_modifications >= self._modification_limit:
			self.apply()


	def apply(self):

		self._storage.write(self.memory)

		self._cache_modifications = 0

	def close(self):

		self.apply()

		self._storage.close()