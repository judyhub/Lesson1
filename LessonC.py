#conditional statements
weight = 50
height = 1.88
bmi = weight /(height*height)

if bmi < 15:
    print("You are very severely underweight")
elif bmi>=15 and bmi<16:
    print("You are severely underweight")
elif bmi>=16 and bmi<18.5:
    print("You are underweight")
elif bmi >= 18.5 and bmi < 25:
    print("Your weight is normal")
elif bmi >= 25 and bmi < 30:
    print("You are overweight")
elif bmi >= 30 and bmi < 35:
    print("You are mmoderately obese")
elif bmi >= 35 and bmi < 40:
    print("You are severely obese")
elif bmi >= 40:
    print("You are very severely obese")
