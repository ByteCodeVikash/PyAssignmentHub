""" 
Take Salary as input from user and Update the salary
of an employee.

1-salary lass than 10,000,5% increment
2-salary between 10,000 and 20,000,10% increment
3-salary between 20,000 and 50,000,15% increment
4-salary more than 50,000,20% increment

"""

salary=int(input("Enter a salary here: "))

if salary<10000:
    increment=salary*0.05
    print("New salary after 5%  increment",salary+increment)
elif 10000<=salary<20000:
    increment=salary*0.10
    print("New salary after 10% incrment",salary+increment)
elif 20000<=salary<50000:
    increment=salary*0.15
    print("new salary after 15% increment",salary+increment)
elif salary>=50000:
    increment=salary*0.20
    print("New salary after 20% increment",salary+increment)
else:
    print("invalid")                