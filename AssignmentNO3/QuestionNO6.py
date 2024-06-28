""" 
Write a function name is_even that takes a number
as a parameter and print "Even" if the number is even and"odd"
if the number is odd .
"""

def is_even(number):
    if number%2==0:
        return "even"
    return "odd"

number=int(input("Enter a number here: "))
x=is_even(number)
print(x)