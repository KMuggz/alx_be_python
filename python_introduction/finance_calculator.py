"""
    Objective:
    Use user input, variables, and arithmetic operations to calculate and provide feedback on a user’s monthly savings and potential future savings without applying conditional statements.

    Task Description:
    You will create a script named finance_calculator.py. This script will calculate the user’s monthly savings based on inputted monthly income and expenses. It will then project these savings over a year, assuming a fixed interest rate, to demonstrate compound interest’s effect on savings.

    Instructions:
        1: User Input for Financial Details:
        Prompt the user for their monthly income: “Enter your monthly income: ”.
        Ask for their total monthly expenses: “Enter your total monthly expenses: ”.

        2: Calculate Monthly Savings:
        Calculate the monthly savings by subtracting monthly expenses from the monthly income.

        3:Project Annual Savings:
        Assume a simple annual interest rate of 5%.
        Calculate the projected savings after one year, incorporating the interest. Use the simplified formula for annual savings projection: (Projected Savings = Monthly Savings * 12 + (Monthly Savings * 12 * 0.05)).

        4:Output Results:
        Display the user’s monthly savings.
        Display the projected annual savings after including interest.
"""

# This is a simple script to calculate monthly savings and projected annual savings with interest

monthly_income = float(input("Enter your monthly income: "))  # User input for monthly income
monthly_expenses = float(input("Enter your total monthly expenses: "))  # User input for monthly expenses

monthly_savings = monthly_income - monthly_expenses  # Calculate monthly savings
projected_annual_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)  # Calculate projected annual savings with interest

print(f'Your monthly savings are: ${monthly_savings}')  # Output monthly savings
print(f'Projected savings after one year, with interest, is: ${projected_annual_savings}')  # Output projected annual savings

