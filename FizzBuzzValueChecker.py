
class FizzBuzzValueChecker:

    @staticmethod
    def checkValue(value):
        if value <= 0:
            raise(IncorrectValueError())

        if value % 3 == 0 and value % 5 == 0:
            return "FizzBuzz"

        if value % 3 == 0: 
            return "Fizz"
        elif value % 5 == 0:
            return "Buzz"
        
        return value
            

class IncorrectValueError(Exception):
    def __init__(self):
        super()