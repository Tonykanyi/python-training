# Continue with the same program and find the person's PAYEE using the taxable income above.
# Find the Kenya PAYEE Tax Rate using THIS LINK
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
relief=2400
if taxable_income<=24000:
    payee=(taxable_income*0.1)-relief
elif(taxable_income>24000 and taxable_income<=32333):
      payee=(taxable_income*0.1)+((taxable_income-24000)*0.25)-relief
else:payee=((2400*0.1)+(8333*0.23)+(taxable_income-32333*0.3))-relief
print(payee)