import logging
import math

# Constants for error messages
DIVIDE_BY_ZERO_ERROR = "Cannot divide by zero"
INPUT_TYPE_ERROR = "Inputs must be numbers"

class Calculator:
    def add(self, a, b):
        """
        Adds two numbers.
        
        :param a: First number
        :param b: Second number
        :return: Sum of a and b
        """
        self._validate_inputs(a, b)
        return a + b

    def subtract(self, a, b):
        """
        Subtracts the second number from the first number.
        
        :param a: First number
        :param b: Second number
        :return: Difference of a and b
        """
        self._validate_inputs(a, b)
        return a - b

    def multiply(self, a, b):
        """
        Multiplies two numbers.
        
        :param a: First number
        :param b: Second number
        :return: Product of a and b
        """
        self._validate_inputs(a, b)
        return a * b

    def divide(self, a, b):
        """
        Divides the first number by the second number.
        
        :param a: First number
        :param b: Second number
        :return: Quotient of a and b
        :raises ValueError: If b is zero
        """
        self._validate_inputs(a, b)
        if b == 0:
            logging.error(DIVIDE_BY_ZERO_ERROR)
            raise ValueError(DIVIDE_BY_ZERO_ERROR)
        return a / b

    def square_root(self, a):
        """
        Returns the square root of a number.
        
        :param a: Number
        :return: Square root of a
        :raises ValueError: If a is negative
        """
        self._validate_single_input(a)
        if a < 0:
            logging.error("Cannot take the square root of a negative number")
            raise ValueError("Cannot take the square root of a negative number")
        return math.sqrt(a)

    def _validate_inputs(self, a, b):
        """
        Validates that inputs are numbers.
        
        :param a: First input
        :param b: Second input
        :raises TypeError: If inputs are not numbers
        """
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            logging.error(INPUT_TYPE_ERROR)
            raise TypeError(INPUT_TYPE_ERROR)

    def _validate_single_input(self, a):
        """
        Validates that the input is a number.
        
        :param a: Input
        :raises TypeError: If input is not a number
        """
        if not isinstance(a, (int, float)):
            logging.error(INPUT_TYPE_ERROR)
            raise TypeError(INPUT_TYPE_ERROR)

# Example usage
if __name__ == "__main__":
    calc = Calculator()
    print(calc.add(1, 2))        # Output: 3
    print(calc.subtract(5, 3))   # Output: 2
    print(calc.multiply(4, 3))   # Output: 12
    print(calc.divide(10, 2))    # Output: 5.0
    print(calc.square_root(16))  # Output: 4.0
