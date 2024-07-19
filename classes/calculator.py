"""
Calculator Module

This module provides a simple Calculator class with basic arithmetic operations.

Classes:
    Calculator: A class with static methods for addition, subtraction, multiplication, and division.
"""

class Calculator:
    @staticmethod
    def add(a, b):
        """
        Add two numbers.

        Args:
            a (float): The first number.
            b (float): The second number.

        Returns:
            float: The sum of the two numbers.
        """
        return a + b

    @staticmethod
    def subtract(a, b):
        """
        Subtract one number from another.

        Args:
            a (float): The number to subtract from.
            b (float): The number to subtract.

        Returns:
            float: The difference of the two numbers.
        """
        return a - b

    @staticmethod
    def multiply(a, b):
        """
        Multiply two numbers.

        Args:
            a (float): The first number.
            b (float): The second number.

        Returns:
            float: The product of the two numbers.
        """
        return a * b

    @staticmethod
    def divide(a, b):
        """
        Divide one number by another.

        Args:
            a (float): The dividend.
            b (float): The divisor.

        Returns:
            float: The quotient of the division.

        Raises:
            ValueError: If the divisor is zero.
        """
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
