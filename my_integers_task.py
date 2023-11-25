#question 1
# Convert a float to an integer with an inbuilt function in Python
# temp = 56.8926 to 57
temp=56.8926
print(round(temp))

#question 2
# Convert the float below to give the results as follows
# temp = 56.8926 to 56.89 
temp=56.8926
temp1=round(temp,2)
print(temp1)


#question 3
# Convert the float below to give the results as follows
# temp = 56.8926 to 56.893 
temp2=56.8926
temp3=round(temp2,3)
print(temp3)

#question 4
# Convert the float below to give the results as follows
# temp=56.8926 to 8.926 
# NB: Use string  slice & concatenation, but have result as float 

temp4=56.8926
temp=str(temp)
temp=temp[3:7]
temp=8+0.926
print(float(temp))
