# Take three inputs from a user, separately. Print the largest of the numbers.
#     Hint: Determine what type of data is taken in as input
# Take as input from a user the temperature if the temperature is above 30°C display “The temperature is too high”, otherwise display “Normal temperature”

num1=int(input("enter number1: "))
num2=int(input("enter number2: "))
num3=int(input("enter number3: "))
if(num1>num2)and(num1>num3):
    print("num1 is larger")
elif(num2>num1)and(num2>num3):
    print("num2 is larger")
else:
    print("num3 is larger")


 #Take as input from a user the temperature if the temperature is above 30°C display “The temperature is too high”, otherwise display “Normal temperature”
temprature=float(input("enter temprature: "))
if(temprature>100):
    print("extreme temp")
elif(temprature>30):
    print("The temperature is too high")
elif(temprature<15.5):
    print("Temp is to low")
else:
    print("Normal temprature")