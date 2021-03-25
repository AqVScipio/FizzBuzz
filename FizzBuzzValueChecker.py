
class FizzBuzzValueChecker:

    @staticmethod
    def checkValue(value):
        if value < 0:
            raise(NegativeValueError())
        elif value == 0:
            raise(Value0Error())
        elif value % 3 == 0: 
            return "Fizz"

class Value0Error(Exception):
    def __init__(self):
        super()

class NegativeValueError(Exception):
    def __init__(self):
        super()