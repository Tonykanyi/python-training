#creating dictionaries
person={
        "name":" John Doe",
        "age":30,
        "location": "Nairobi",
        "email" :"johndoe@mail.com"
}
#accessing values inside a dictionary(we use keys)

print(person["age"])

#updating values in a dictionary
person["age"]=50
person["name"]="Kanyi"
person["location"]="Mombasa"
print (person)

#Adding a new key value pair
person["gender"]="Male"
print (person)
#dictionary methods
print(person.get("age"))

new_data={"course":"education","campus":"nairobi"}
person.update(new_data)
print(person)

person.pop("location")
print(person)