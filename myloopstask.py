#Write a program that displays a numbers 1 to 50 inside a list.

#From 1 above display the ones divisible by 7 or 5 inside a list.

#Find sum and average of values in the range between 10 to 40.

#Put in a list the first 10 odd numbers between 10 to 50. 



# Display numbers 1 to 50 inside a list
numbers_list = []
for i in range(1, 51):
    numbers_list.append(i)
print("Numbers 1 to 50 inside a list:")
print(numbers_list)

# Display numbers divisible by 7 or 5 inside a list
divisible_list = []
for num in range(1, 51):
    if num % 7 == 0 or num % 5 == 0:
        divisible_list.append(num)
print("\nNumbers divisible by 7 or 5 inside a list:")
print(divisible_list)

# Find sum and average of values in the range between 10 to 40
values=[]
for i in range(10,41):
    values.append
print(values)


sumation=sum(values)
avarage=sumation/len(values)
print(f"{sumation} sum")
print(f"{avarage} avarage")


# Put in a list the first 10 odd numbers between 10 to 50
main=[]
for i in range(10,51):
    if i%2!=0:
        main.append(i)
        if len(main)==10:
            break
print(f"{main} main")



