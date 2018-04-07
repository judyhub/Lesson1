# if
# if else
# else if

#We need to convert weight and height to float
# By default they are in strings format

print("WELCOME TO BMI CALC VI")

name = input("Enter your Name")
weight = float(input("Enter your Weight"))
height = float(input("Enter your Height"))

print ("YOUR NAME IS", name)
print ("YOUR WEIGHT IS", weight)
print ("YOUR HEIGHT IS", height)

bmi = weight/(height*height)
print("YOUR BMI IS", bmi)

if bmi < 18:
    print("YOUR BMI IS TOO LOW!") # Print if true
elif bmi > 18 and bmi < 21:
    print("THAT IS NORMAL")
elif bmi >= 21 and bmi < 25:
    print("THAT IS TOO HIGH!")
else:
    print("EVERYTHING IS FINE") # Print if false

print("THANK YOU!")