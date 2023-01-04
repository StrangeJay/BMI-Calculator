# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# Formula for BMI is weight(kg) / height**2

# Convert weight and height to floats

w = float(weight)
h = float(height)

BMI = w / (h**2)

print(int(BMI))
