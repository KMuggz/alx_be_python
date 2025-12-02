class Calculator:
    """
    A class demonstrating the use of static methods and class methods.
    """
    # Class Attribute: shared by all instances and the class itself.
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """
        Static Method: Doesn't access class-specific or instance-specific data.
        It's just a regular function logically grouped within the class namespace.
        The method receives no special first argument (like self or cls).
        """
        # Performs a simple calculation.
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        Class Method: Binds the method to the class, not the instance.
        It receives the class itself (conventionally named 'cls') as the first argument.
        This allows it to access and modify class attributes.
        """
        # Accesses the class attribute 'calculation_type' via the 'cls' parameter.
        print(f"Calculation type: {cls.calculation_type}")
        # Performs a calculation.
        return a * b

