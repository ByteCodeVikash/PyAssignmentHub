""" 
Write a function named is_odd_even that determines if
a number is odd or even without using the modulo operator(%)
Hint:Use division or subtraction.

"""


def is_odd_even(number):
    if (number//2)*2==number:
        print("even")
    else:
        print("odd")    



number=int(input("Enter a number here: "))
is_odd_even(number)    