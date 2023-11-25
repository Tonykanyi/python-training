person=["Abigael Murungi",18,"female","Nairobi","0777777"]
print(person[2])

#TASK: Create a List of days of the Week. Print the day today using an index.
week=["Monday","Tuesday","Wednesday","Thurday","Friday","Saturday","Sunday"]
print(week[2])


group_list=[[1,2,3,4,5,6,7],"tony","tosh","hamo"]
print(group_list)

add_list=week+group_list
print(add_list)
#checking membership

print("friday" in add_list)

#how to update in a list
group_list=[[1,2,3,4,5,6,7],"tony","tosh","hamo"]
group_list[-1]="friday"
#how to delete
del group_list[1]
print(group_list)

#how to insert a character inside a list
group_list.append("tuesday")
print(group_list)
