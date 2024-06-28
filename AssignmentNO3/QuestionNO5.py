""" 
Write a function named personal_greet that takes a name as a
parameter and prints a greeting message with that name.for example
personal_greet("Alice")should print "Hello,Alice!".

"""

def personal_greet(name:str)->str:
    return f"Hello,{name}!"

name=input("Enter a your name here: ")
x=personal_greet(name)
print(x)