# Write a program that takes the date of birth of a person and the program outputs the age in terms of years,months,days TODAY.
from datetime import datetime

# Input the date of birth from the user in the format YYYY-MM-DD
dob_input = input("Enter your date of birth (YYYY-MM-DD): ")

# Convert the input string to a datetime object
dob = datetime.strptime(dob_input, "%Y-%m-%d")

# Get today's date
today = datetime.now()

# Calculate the difference between today's date and the birth date
age = today - dob

# Calculate years, months, and days from the age difference
years = age.days // 365
remaining_days = age.days % 365
months = remaining_days // 30
days = remaining_days % 30

# Output the age
print(f"Your age is: {years} years, {months} months, and {days} days")
