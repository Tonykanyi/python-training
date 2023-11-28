# Continue with the program above, then use  the gross salary to find the NSSF. 
# To find the Kenya NSSF Rate using. Compute NSSF using 6% of the Gross Salary. 
# BUT ONLY A MAXIMUM OF 18,000 CAN BE USED IN NSSF. 

basic_salary=int(input("enter your basic salary: "))
benefits=int(input("enter your benefits: "))
gross_salary=basic_salary+benefits
nssf_rate=0.06
if(gross_salary>18000 and gross_salary<18000):
         nssf=(gross_salary*nssf_rate)
else:
    gross_salary=18000
    nssf=(gross_salary*nssf_rate)
print(nssf)
    
