#calculating gross salary

def calc_gross(benefits,basic_salary):
    gross_salary=basic_salary+benefits
    return gross_salary
calc_gross(1000,10000)

#
basic_salary=int(input("enter your basic salary: "))
benefits=int(input("enter your benefits: "))
gross_salary=calc_gross(benefits,basic_salary)
print(f"gross salary is: {gross_salary}")

#15 .Write a program that takes input of someone's basic salary and benefits, adds them to find the gross salary then 
# uses  the gross salary to find the NHIF. 
#To find the Kenya NHIF Rate using THIS LINK:  

def calc_nhif(gross_salary):
    if gross_salary<5999:
        nhif=150
    elif gross_salary<7999:
        nhif=300
    elif gross_salary<11999:
        nhif=400
    elif gross_salary<14999:
        nhif=500
    elif gross_salary<19999:
        nhif=600
    elif gross_salary<24999:
        nhif=750
    elif gross_salary<29999:
        nhif=850
    elif gross_salary<34999:
        nhif=900
    elif gross_salary<39999:
        nhif=950
    elif gross_salary<44999:
        nhif=1000
    elif gross_salary<49999:
        nhif=1100
    elif gross_salary<59999:
        nhif=1200
    elif gross_salary<69999:
        nhif=1300
    elif gross_salary<79999:
        nhif=1400
    elif gross_salary<89999:
        nhif=1500
    elif gross_salary<99999:
        nhif=1600
    else:
        nhif=1700
    return nhif 
final_nhif=calc_nhif(gross_salary)
print(f"nhif is: {final_nhif}")

#16Continue with the program above, then use  the gross salary to find the NSSF. 
#To find the Kenya NSSF Rate using. Compute NSSF using 6% of the Gross Salary. BUT ONLY A MAXIMUM OF 18,000 CAN BE USED IN NSSF. 
def calc_nssf(gross_salary,nssf_rate=0.06):
    if(gross_salary>18000):
        nssf=(gross_salary*nssf_rate)
    else:
        nssf=(gross_salary*nssf_rate)
    return nssf
final_nssf= calc_nssf(gross_salary,nssf_rate=0.06)
print(f"nssf is: {final_nssf}")

#17Continue with the same program and calculate an individual’s NHDF using:
#i.e NHDF = gross_salary *  0.015

def calc_nhdf(gross_salary,nhdf_rate=0.015):
    start_nhdf = gross_salary * nhdf_rate
    return start_nhdf
final_nhdf=calc_nhdf(gross_salary,nhdf_rate=0.015)
print(f"nhdf is: {final_nhdf}")

#18> Calculate the taxable income.
#i.e taxable_income = gross salary - (NSSF + NHDF)
def calc_taxable_income(gross_salary,final_nssf,final_nhdf):
    taxable_income=gross_salary-(final_nssf+final_nhdf)
    return taxable_income
final_taxable_income=calc_taxable_income(gross_salary,final_nssf,final_nhdf)
print(f"taxable income is: {final_taxable_income}")

#19Continue with the same program and find the person's PAYEE using the taxable income above.
#Find the Kenya PAYEE Tax Rate using THIS LINK

def calc_payee(final_taxable_income):
    relief=2400
    if final_taxable_income<=24000:
        payee=relief-relief
    elif(final_taxable_income>24000 and final_taxable_income<=32333):
        payee=(final_taxable_income*0.1)+((final_taxable_income-24000)*0.25)-relief
    else:payee=((2400*0.1)+(8333*0.23)+(final_taxable_income-32333*0.3))-relief
    return payee
final_payee=calc_payee(final_taxable_income)
print(f"payee is: {final_payee}")

#20Continue with the same program and calculate an individual’s Net Salary using:
#net_salary = gross_salary - (nhif + nhdf +  nssf + payee)

def calc_net_salary(gross_salary,final_nhif,final_nssf,final_nhdf,final_taxable_income,final_payee):
    net_salary=gross_salary-(final_nhif+final_nssf+final_nhdf+final_payee)
    return net_salary
final_net_salary=calc_net_salary(gross_salary,final_nhif,final_nssf,final_nhdf,final_taxable_income,final_payee)
print(f"net salary is: {final_net_salary}")
