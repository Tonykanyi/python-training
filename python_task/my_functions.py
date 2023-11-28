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