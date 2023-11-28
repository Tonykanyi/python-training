# Write a program that prints the largest of 4 inputs taken in from a user. 
# Assume that the user would not enter any two numbers which are the same.
num1=int(input("enter number 1: "))
num2=int(input("enter number 2: "))
num3=int(input("enter number 3: "))
num4=int(input("enter number 4: "))

if num1>num2 and num1!=num2 and num1>num3 and num1!=num3 and num1> num4 and num1!=num4:
    print("num1 is larger")
elif num2>num1 and num2!=num1 and num2>num3 and num2!=num3 and num2> num4 and num2!=num4:
    print("num2 is larger")
elif num3>num2 and num3!=num2 and num3>num1 and num3!=num1 and num3> num4 and num3!=num4:
    print("num3 is larger")
else:
    print("num4 is larger")