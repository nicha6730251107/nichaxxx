"""
BMI Calculator (20 points)
Write a program that:
Asks for weight in kilograms
Asks for height in meters
Calculates BMI using formula: BMI = weight / (height²)
Displays BMI with 1 decimal place
Shows BMI category based on the ranges below
BMI Categories:
Below 18.5: Underweight
18.5 - 24.9: Normal weight
25.0 - 29.9: Overweight
30.0 and above: Obese
"""
weight = float(input("Weight: "))
height = float(input("Height: "))
bmi = weight / height ** 2
printf("Your BMI: ", bmi)
if bmi < 18.5:
   printf("Underweight")
elif bmi >= 8.5 and bmi <=24.9:
   printf("normalweight")
elif bmi >= 25 and bmi <=29.9:
   printf("Overweight")
elif bmi >=30:
   printf("Obese")