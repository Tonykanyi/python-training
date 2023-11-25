n="10"
for i in n:
    print(i)
    #looping throgh a list

nov_intake=["Anthony","Tosh","Ramadhan","Cornelias","Harman","Lilian","Bilal","iano","abigael"]

for i in nov_intake:
    if i=="iano":
        break
    print(i)
#looping through a control statement
for i in range(20):
    if i==10:
        continue
    print(i)


    #looping through a dictionary
    person={
        "name":" John Doe",
        "age":30,
        "location": "Nairobi",
        "email" :"johndoe@mail.com"
}
    for key,value in person.items():
            print(key,value)