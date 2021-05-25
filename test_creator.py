
from typing import Callable, Mapping, Tuple, Any

class Query:

	def __init__(self, test: Callable, hashval: Tuple):
		self._test = test
		self._hash = hashval

	def __call__(self, value: Mapping) -> bool:

		return self._test(value)

	def __hash__(self):

		return hash(self._hash)

	def __repr__(self):

		return "QueryInstance"	

	def __eq__(self, other: object):
		if isinstance(other, Query):
			return self._hash == other._hash

		return False


class QueryIns(Query):

	def __init__(self):

		self._path = ()

	def _generate_test(self, test: Callable, hashval: Tuple) -> Query:

		# Create running function
		return Query(
			lambda value: test(value),
			hashval
		)

	def __eq__(self, rhs: Any):

		return self._generate_test(
			lambda value: value == rhs,
			("==", self._path, rhs)
		)

def main() -> int:

	query = QueryIns()

	print((query == 2))

	return 0

if __name__ == "__main__":
	exit(main())