
class TestInstance:

    def __init__(self, test, value):
        self._test = test
        self._value = value

    def __call__(self, value) -> bool:

        return self._test(value)



class Query:

    def __init__(self, value) -> None:

        self._value = value


    def _generate_test(self, test):

        return 

    def __eq__(self, rhs):

        return self._generate_test(
            lambda value: value == rhs
        )