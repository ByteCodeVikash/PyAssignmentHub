""" 
Write a program to calculate bill. Ask the final amount from the user
You have to give discount and print the final bill after discount

50000 above - 30 % discount
40000-49999- 25 % discount
30000- 39999 - 20 % discount
10000- 29999 - 10 % discount

1- 9999 - No discount

print the discount and the final amount to be paid

Example:-
Enter a bill amount=80000
you got 30 % discount
Your final bill is Rs.56000


"""


amount=int(input("Enter a amount here: "))

if amount >= 50000:
    discount_percentage=30
elif 40000 <= amount  <= 49999:
    discount_percentage=25
elif 30000 <= amount <= 39999:
    discount_percentage=20
elif 10000 <= amount <= 29999:
    discount_percentage=10
else:
    discount_percentage=0


discount_amount=(discount_percentage/100)*amount
final_amount=amount-discount_amount

print(f"You got {discount_percentage}% discount")
print(f"Your final bill is Rs.{final_amount}")


    