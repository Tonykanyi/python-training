# Create a file called mydstask.py and attempt the below questions:
# my_ds = [23, “Jane”, (560), [“Lesson”, “Maths”, {“currency” : “KES”}], 987, (76,”John”)]
# 1. Print KES
# 2. Print 560
# 3. Print Maths
# 4. In the dictionary with the key currency, add another key “amount” with value 90
# 5. Reverse 987 to 789 without using an inbuilt -method or Assigning 789 manually.
#      Hint: Strings can be reversed using [::]
# 6. Change the name “John” to “Jane” . 

my_ds=[23,"Jane",(560),["lesson","Math",{"currency":"KES"}],987,(76,"John")]

#question1
print(my_ds[3][2]["currency"])

#question 2
print(my_ds[2])

#question 3
print(my_ds[3][1])

#question 4
my_ds[3][2]["amount"]=90
print(my_ds)

#question 5
my_ds[4]=str(my_ds[4])
print(my_ds[4][2::-1])

#question 6
my_ds[5]=list(my_ds[5])
my_ds[5][1]="Jane"
my_ds[5]=tuple(my_ds[5])
print(my_ds)