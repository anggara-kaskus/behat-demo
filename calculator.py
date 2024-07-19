import logging

# Constants for error messages
DIVIDE_BY_ZERO_ERROR = "Cannot divide by zero"

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

    def _validate_inputs(self, a, b):
        """
        Validates that inputs are numbers.
        
        :param a: First input
        :param b: Second input
        :raises TypeError: If inputs are not numbers
        """
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Inputs must be numbers")

# Example usage
if __name__ == "__main__":
    calc = Calculator()
    print(calc.add(1, 2))        # Output: 3
    print(calc.subtract(5, 3))   # Output: 2
    print(calc.multiply(4, 3))   # Output: 12
    print(calc.divide(10, 2))    # Output: 5.0
