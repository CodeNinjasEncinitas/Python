import math

while True:
    radius = input("Enter a Radius: ")
    radius = int(radius)
    area = (math.pi)*(radius**2)
    print(f"Area = PI x Radius**2 = 3.14159 x {radius}**2 = {area}")
    print("----------------------------------------------")
