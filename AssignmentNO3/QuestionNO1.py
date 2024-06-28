"""
Write a python function to find the miximum and minimum
of three numbers.use 3 parameters. make 2 different function named
as maxi and mini
 
"""

#maximum
def maxi(num1:int,num2:int,num3:int)->int:
    if num1>num2 and num1>num3:
        return num1
    elif num2>num1 and num2>num3:
        return num2
    return num3

num1=int(input("Enter a first number here: "))
num2=int(input("Enter a second number here: "))
num3=int(input("Enter a third number here: "))

x=maxi(num1,num2,num3)
print(x)

#minimum

def mini(num1:int,num2:int,num3:int)->int:
    if num1<num2 and num1<num3:
        return num1
    elif num2<num1 and num2<num3:
        return num2
    return num3

num1=int(input("Enter a first number here: "))
num2=int(input("Enter a second number here: "))
num3=int(input("Enter a third number here: "))

y=mini(num1,num2,num3)
print(y)



#-------------------------------------------------------------------------------
# Maximum function
def maxi(num1: int, num2: int, num3: int) -> int:
    return max(num1, num2, num3)

# Minimum function
def mini(num1: int, num2: int, num3: int) -> int:
    return min(num1, num2, num3)

# User inputs
num1 = int(input("Enter the first number here: "))
num2 = int(input("Enter the second number here: "))
num3 = int(input("Enter the third number here: "))

# Find and print maximum
x = maxi(num1, num2, num3)
print("Maximum number is:", x)

# Find and print minimum
y = mini(num1, num2, num3)
print("Minimum number is:", y)
