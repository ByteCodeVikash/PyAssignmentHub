"""
A student will not be allowed to sit in exam if his/her attendance is less
than 75%

Take following input from user

* Number of classes held
* Number of classes attended

1. Print percentage of class attended
2. Print is student is allowed to sit in exam or not.

"""

classes_held=int(input("Enter a Number of classes held: "))
classes_attended=int(input("Enter a number of classes attended: "))

percentange=(classes_attended/classes_held)*100

print("Percentage of class attended",percentange)

if percentange >=75:
    print("Yes,student is allowed to sit in exam ")
else:
    print("No,the student is not allowed to sit in exam")    