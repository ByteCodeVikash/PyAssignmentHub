""" 
Attempt Week1-Assignment2(Q6)and Week1-Assignment2(Q7)
using function

#Question no 6--->

Ask 4 numbers from user.Make sure all the numbers
entered by user are different .print which
number is the smallest.

#Question no 7--->

Take Salary as input from user and Update the salary
of an employee.

1-salary lass than 10,000,5% increment
2-salary between 10,000 and 20,000,10% increment
3-salary between 20,000 and 50,000,15% increment
4-salary more than 50,000,20% increment


"""

#Question no -6

def check_no(num1:int,num2:int,num3:int,num4:int)->int:

    if num1<num2 and num1<num3 and num1<num4:
        return num1
    elif num2<num1 and num2<num3 and num2<num4:
        return num2
    elif num3<num1 and num3<num2 and num3<num4:
        return num3
    return num4

num1=int(input("Enter a first number here: "))
num2=int(input("Enter a second number here: "))
num3=int(input("Enter a third number here: "))
num4=int(input("Enter a fourth number here: "))

x=check_no(num1,num2,num3,num4)
print(x,"is a smallest number")

#Question no -7

def update_salary(salary:int)->int:
    if salary<10000:
        incremnet=salary*0.05
        print("New increment salary after 5% increment",incremnet+salary)
    elif 10000<=salary <=20000:
        incremnet=salary*0.10
        print("New salary after 10% increment",incremnet+salary)
    elif 20000<= salary <=50000:
        incremnet=salary*0.15
        print("New salary after 15% increment",incremnet+salary)
    elif salary>=50000:
        incremnet=salary*0.20
        print("New salary after 20% increment",incremnet+salary)
    else:
        print("invalid")    

salary=int(input("Enter a salary here: ")) 
update_salary(salary)        


#------------------------------------------------------------------------------

#Question 6: Smallest Number
def check_no(num1: int, num2: int, num3: int, num4: int) -> int:
    return min(num1, num2, num3, num4)

num1 = int(input("Enter the first number here: "))
num2 = int(input("Enter the second number here: "))
num3 = int(input("Enter the third number here: "))
num4 = int(input("Enter the fourth number here: "))

smallest = check_no(num1, num2, num3, num4)
print(smallest, "is the smallest number")


#Question 7: Update Salary

def update_salary(salary: int) -> int:
    if salary < 10000:
        increment = salary * 0.05
        new_salary = salary + increment
        increment_percentage = 5
    elif 10000 <= salary <= 20000:
        increment = salary * 0.10
        new_salary = salary + increment
        increment_percentage = 10
    elif 20000 <= salary <= 50000:
        increment = salary * 0.15
        new_salary = salary + increment
        increment_percentage = 15
    else:
        increment = salary * 0.20
        new_salary = salary + increment
        increment_percentage = 20

    print(f"New salary after {increment_percentage}% increment: {new_salary}")
    return new_salary

salary = int(input("Enter a salary here: ")) 
update_salary(salary)
