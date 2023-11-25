# Clean up the following variable to give the clean version in lower case. Using inbuilt methods in the str class 
# name = “  JOHn  .“ to “john”
name="   JOHn   ."
name=name.lower().replace("."," ").strip()
print(name)