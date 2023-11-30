#how to create functions
def calc_gross(benefits,basic_salary):
    gross_salary=basic_salary+benefits
    return gross_salary
calc_gross(1000,10000)

#
basic_salary=int(input("enter your basic salary: "))
benefits=int(input("enter your benefits: "))
gross_salary=calc_gross(benefits,basic_salary)
print(gross_salary)

def area_triangle(a,b):
    area=(a*b)/2
    return(area)
base=float(input("enter base"))
height=float(input("enter height"))
triangle1=area_triangle(base,height)
print(triangle1)

#write a function that checks if a  number is even or odd from the users input
def check_number(a):
    if(a%2==0):
        num="even"
    else:
        num="odd"
    return num

number=int(input("enter number: "))
nums=check_number(number)
print(nums)