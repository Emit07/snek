

class Document:

	def __init__(self, storage, document_id):
		"""
		Passes through the storage variable for reading
		Sets up the id to request document from database
		"""		

		self._storage = storage

		self._id = document_id

	def insert(self, value: dict) -> None:
		content = self._storage.read()
		content.append(value)

		return content


	def remove(self):
		pass