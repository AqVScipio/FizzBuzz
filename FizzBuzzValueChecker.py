
class FizzBuzzValueChecker:

    @staticmethod
    def checkValue(value):
        if(value < 0):
            raise(NegativeValueError())
        else:
            raise(Value0Error())

class Value0Error(Exception):
    def __init__(self):
        super()

class NegativeValueError(Exception):
    def __init__(self):
        super()