
from typing import Tuple, Callable, Any, Union, List


class QueryInstance: 

	def __init__(self, test: Callable, value):

		self._test = test
		self._value = value


	def __call__(self, value):

		return self._test(value)


	def __hash__(self):

		return hash(self._value)


	def __repr__(self):

		return str(self._value)


	def __eq__(self, other: object):
		if isinstance(other, QueryInstance):
			return self._value == other._value

		return False


class Query(QueryInstance):

	def __init__(self) -> None:

		self._path = ()

		def notest(_):
			raise RuntimeError("Empty Query")

		super().__init__(
			test=notest,
			value=(None,)
		)


	def __repr__(self):
		return "{}()".format(type(self).__name__)


	def __getattr__(self, item: str):

		query = type(self)()

		query._path = self._path + (item,)

		query._value = ("path", query._path)

		return query


	def __getitem__(self, item: str):

		return self.__getattr__(item)


	def _generate_test(
		self,
		test: Callable,
		value: Tuple,
		allow_empty_path: bool = False
	) -> QueryInstance:

		if not self._path and not allow_empty_path:
			raise ValueError("Query has no path")
			
		return QueryInstance(
			lambda value: test(value),
			value
		)


	def __eq__(self, rhs: Any):

		return self._generate_test(
			lambda value: value == rhs,
			("==", self._path, rhs)
		)

def where(key: str) -> Query:

	return Query()[key]

