#Write a program that takes two numbers as input and checks if the first number is divisible by the second.

num1=int(input("Enter a first number here: "))
num2=int(input("Enter a second number here: "))

if num1 % num2 == 0:
    print("Yes,the first number is divisible by the second numbere")
else:
    print("No,the first number is not divisible by the second number")    