""" 
Write a python program that takes a student's score as input and
print the corresponding grade.use the following grading scale.

A: 90-100
B: 80-89
C: 70-79
D: 60-69
F: Below 60
"""

score=int(input("Enter a your score: "))

if 90 <= score <= 100:
    print("A grade")
elif 80 <= score <= 89:
    print("B grade") 

elif 70 <= score <= 79:
    print("C grade")

elif 60 <= score <= 69:
    print("D grade") 

elif score <= 60:
    print("Fail")
else:
    print("Invalid score")           