# this script 'arithmetic_operations.py' will accept arguments for basic arithmetic functions

def perform_operation(num1: float, num2: float, operation: str) -> float | str:
    """
    Performs a specified arithmetic operation on two numbers.

    Parameters:
        num1 (float): The first number.
        num2 (float): The second number.
        operation (str): The operation to perform.
                        Must be 'add', 'subtract', 'multiply', or 'divide'.

    Returns:
        float: The result of the operation.
        str: An error message if the operation is invalid or division by zero occurs.
    """

    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Cannot divide by zero."
    else:
        return f"Error: Invalid operation '{operation}'. Must be 'add', 'subtract', 'multiply', or 'divide'."

