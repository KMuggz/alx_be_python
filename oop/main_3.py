# main_3.py (Provided for Testing)
from class_static_methods_demo import Calculator

def main():
    # Using the static method. It can be called directly on the class.
    sum_result = Calculator.add(10, 5)
    print(f"The sum is: {sum_result}")

    # Using the class method. It can also be called directly on the class.
    # It prints the class attribute before performing the multiplication.
    product_result = Calculator.multiply(10, 5)
    print(f"The product is: {product_result}")

if __name__ == "__main__":
    main()