
class FizzBuzzValueChecker:

    @staticmethod
    def checkValue(value):
        raise(Value0Error())

class Value0Error(Exception):
    def __init__(self):
        super()