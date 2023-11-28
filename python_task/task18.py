basic_salary=int(input("enter your basic salary: "))
benefits=int(input("enter your benefits: "))
gross_salary=basic_salary+benefits
NHDF = gross_salary *  0.015
nssf_rate=0.06
if(gross_salary>18000 and gross_salary<18000):
         nssf=(gross_salary*nssf_rate)
else:
    gross_salary=18000
    nssf=(gross_salary*nssf_rate)
taxable_income = gross_salary - (nssf + NHDF) 
print(taxable_income)