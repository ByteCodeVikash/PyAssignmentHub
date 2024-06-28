""" 
Write a function named check_number that takes a number
and prints whether it is positive,negative or zer0.

"""

def check_number(number):
    if number>0:
        print(number,"is a positive")
    elif number<0:
        print(number,"is a negative ")
    else:
        print(number,"is a zero")

number=int(input("Enter a number here: "))
check_number(number)                