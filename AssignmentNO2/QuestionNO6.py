"""
Ask 4 numbers from user.Make sure all the numbers
entered by user are different .print which
number is the smallest.

"""

num1=int(input("Enter a first number here: "))
num2=int(input("Enter a second number here: "))
num3=int(input("Enter a third number here: "))
num4=int(input("Enter a fouth number here: "))

if num1<num2 and num1<num3 and num1<num4:
    print(num1,"is a smallest number")
elif num2<num1 and num2<num3 and num2<num4:
    print(num2,"is a smallest number")
elif num3<num1 and num3<num2 and num3<num4:
    print(num3,"is a smallest number")
else:
    print(num4,"is a smallest number")            