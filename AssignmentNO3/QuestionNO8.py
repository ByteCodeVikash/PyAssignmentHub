""" 
Create a Function named simple_calculator that
takes three parameters:two numbers and an operation
(addition or subtraction)represented by '+'or'-',and
prints the result of the operation.

"""

def simple_calculator(num1: int, num2: int, operation: str):
    if operation == '+':
        total = num1 + num2
        print(total)
    elif operation == '-':
        total = num1 - num2
        print(total)
    else:
        print("Invalid operation. Please choose '+' or '-'.")

num1 = int(input("Enter the first number here: "))
num2 = int(input("Enter the second number here: "))
operation = input("Choose any one operation '+' or '-': ")

simple_calculator(num1, num2, operation)
