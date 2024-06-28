"""
Attempt the same bill calculator question(week 1-Assignment 2-Q5)
but using function.try calling function with different bill amount
as a parameter and check the output

#Question

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

def bill_calculate(bill: int) -> int:
    if bill > 50000:
        discount_percentage = 30
    elif 40000 <= bill <= 49999:
        discount_percentage = 25
    elif 30000 <= bill <= 39999:
        discount_percentage = 20
    elif 10000 <= bill <= 29999:
        discount_percentage = 10
    else:
        discount_percentage = 0

    discount_amount = (discount_percentage / 100) * bill  
    final_amount = bill - discount_amount 
    print(f"You got {discount_percentage}% discount")
    print(f"Your final bill is Rs.{final_amount}")
    return final_amount

# User input
bill = int(input("Enter a bill amount here: ")) 
x = bill_calculate(bill)
print(x) 