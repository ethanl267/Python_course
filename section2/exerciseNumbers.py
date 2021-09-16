import math

radius = float(input("Type the radius of the circle; "))
area = math.pi * (radius ** 2)
circumference = 2 * math.pi * radius

print("The area of the circle is",round(area))
print("The area of the circumference is", round(circumference))