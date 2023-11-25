#first_name="  Joh.n"  last_name="   Do,e" Clean up and display Full name i.e John Doe
first_name="Joh.n"
last_name="Do,e"
cleaned_first_name = first_name.strip().replace(".", "").capitalize()
cleaned_last_name = last_name.strip().replace(",", "").capitalize()
full_name = f"{cleaned_first_name} {cleaned_last_name}"

# Display the result
print("Full name:", full_name)