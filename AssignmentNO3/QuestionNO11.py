""" 
Write a function named calculate_interest that takes the
principal,rate of interest ,and time as parameters and prints the
simple interest calculated

"""

def calculate_interest(principal, rate_of_interest, time):
    simple_interest = (principal * rate_of_interest * time) / 100
    print("Simple Interest:", simple_interest)

principal = float(input("Enter principal amount: "))
rate_of_interest = float(input("Enter rate of interest (in %): "))
time = float(input("Enter time period (in years): "))

calculate_interest(principal, rate_of_interest, time)

