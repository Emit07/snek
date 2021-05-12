

class Document:

	def __init__(self):
		pass

	def insert(self, data: dict) -> int:

        if not isinstance(data, dict):
            raise ValueError("Value is not dictionary type.")

    def _update_database(self, mode):
    	pass