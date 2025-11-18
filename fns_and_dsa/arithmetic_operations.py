# this script 'arithmetic_operations.py' will accept arguments for basic arithmetic functions

def perform_operation(num1: float, num2: float, operation: str) -> float | str: # the return value may be either a float OR a string. (union type)
    """
    Perform a basic arithmetic operation between two numbers.

    Args:
        num1: The first number--float.
        num2: The second number--float.
        operation: The arithmetic operation--string ('add', 'subtract', 'multiply', 'divide').

    Returns:
        The result of the successful numerical operations as a float or a string indicating division by zero.
    """
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        # Handle division by zero explicitly
        if num2 == 0:
            return "Error: Cannot divide by zero"
        return num1 / num2
    else:
        # Handle unrecognized operation type
        return f"Error: Invalid operation '{operation}'"



