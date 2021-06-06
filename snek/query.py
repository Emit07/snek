
from typing import Tuple, Callable, Any, Union, List


class QueryInstance: 

	def __init__(self, test: Callable, value):
		"""
		This function sets up the global variables for the test and the
		Value that needs to be tested
		"""

		self._test = test
		self._value = value


	def __call__(self, value):

		# When the instance is called it runs the test
		return self._test(value)


	def __repr__(self):

		# Returns the value aiming for
		return str(self._value)


class Query(QueryInstance):

	def __init__(self) -> None:
	
		# Key that object is aiming for
		self._key = None

		self._query_cache = []

		# Returns error if test is empty
		def notest(_):
			raise RuntimeError("Empty Query")

		# Passes in values for a null test
		super().__init__(
			test=notest,
			value=(None,)
		)


	def __repr__(self):

		return "{}()".format(type(self).__name__)


	def __getattr__(self, item: str):
		# Creates a new query instance for comparing 

		# Subclass
		query = type(self)()

		query._key = item

		query._value = query._key

		return query


	def __getitem__(self, item: str):

		return self.__getattr__(item)
		

	def _generate_test( self, test: Callable, value: Tuple) -> QueryInstance:

		if self._key is None:
			raise ValueError("Query has no path")
			
		# Creates a query instance
		return QueryInstance(
			lambda value: test(value),
			("==", self._key, value)
		)



	"""
	Below this comment are all the magic methods used for comparing the query.
	All these methods contain the same boiler plate only changing the comparison
	"""

	def __eq__(self, other: Any):
		"""
		Is equal to "==" method, creates test for this comparison
		"""

		# Basic test function to compare value
		def test(value):
			# TODO could be a simple lambda, figure it out

			# Checks if value exists and the returns if it exists
			if self._value in value:
				return value[self._value] == other

			return False


		# TODO Fix not needed stuff
		return self._generate_test(
			test,
			("==", self._key, other)
		)


	def __ne__(self, other: Any):
		"""
		Not equal to "!=" method, creates test for this comparison
		"""

		def test(value):

			if self._value in value:
				return value[self._value] != other

			return False

		return self._generate_test(
			test,
			()
		)


	def __lt__(self, other: Any): 
		"""
		Less than "<" method, creates test for this comparison
		"""

		def test(value):

			if self._value in value:
				return value[self._value] < other

			return False

		return self._generate_test(
			test,
			()
		)


	def __gt__(self, other: Any):
		"""
		Greater than to ">" method, creates test for this comparison
		"""

		def test(value):

			if self._value in value:
				return value[self._value] > other

			return False

		return self._generate_test(
			test,
			()
		)


	def __le__(self, other: Any):
		"""
		Less than or equal to "<=" method, creates test for this comparison
		"""

		def test(value):

			if self._value in value:
				return value[self._value] <= other

			return False

		return self._generate_test(
			test,
			()
		)


	def __ge__(self, other: Any):
		"""
		Greater than or equal to ">=" method, creates test for this comparison
		"""

		def test(value):

			if self._value in value:
				return value[self._value] >= other

			return False

		return self._generate_test(
			test,
			()
		)


def where(key: str) -> Query:
	"""
	Different syntax for query
	"""

	return Query()[key]

