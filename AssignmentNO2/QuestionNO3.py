#Write a program to check if number is divisivle by 2 and 3 but not 8.

number=int(input("Enter a number here: "))

if (number%2==0) and (number%3==0) and (number % 8 !=0):
    print("Yes ,the number is divisible by 2 and 3 but not 8")
else:
    print("NO,this is not divisible by 2 and 3 ")    