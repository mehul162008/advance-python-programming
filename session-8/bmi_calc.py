import math

weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in meters: "))

height_squared = math.pow(height, 2)

bmi = weight / height_squared

print("BMI:", round(bmi, 2))