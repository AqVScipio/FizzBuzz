
class FizzBuzzValueChecker:

    @staticmethod
    def checkValue(value):
        if value == 0 or value < 0:
            raise(IncorrectValueError())
        elif value % 3 == 0: 
            return "Fizz"
        elif value % 5 == 0:
            return "Buzz"

class IncorrectValueError(Exception):
    def __init__(self):
        super()