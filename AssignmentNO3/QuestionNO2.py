""" 
Attempt the same leap year question(weak 1 Assignment 2-Q8)
but using function.try calling function with different years as a 
parameter and check the output

#Question---

An extra day is added to the calendar almost every four years as
February 29,and the day is called a leap day.A leap year contains a leap
day.

These are the conditions used to identify leap years:
1-if the year can be evenly divided by 4,it is then a leap year
2-but if the year is evenly divided by 4 and also by 100 ,then it is NOT a leap year
3-but if the year is evenly divided by 4 and also by 400,then it is a leap year

this means the years 2000 and 2400 are leap years,while 1800,1900,
2100,2200,2300 and 2500 are NOT leap years.

Ask a year input from user.And tell if the year entered by user is leap or not.

"""

def check_year(year)->int:
    if (year%4==0 and year%100!=0) or (year%400==0):
        print(year,"is a leap year")
    else:
        print(year,"is not a leap year")

year=int(input("Enter a year here: "))
check_year(year)

