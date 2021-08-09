"""
### Excercise 1.5 | Triangle area (approx. 1 hours)
Write a program that will ask a user for the lengths of the sides of a triangle.
Check if it's possible to create a triangle from those lengths and if so, calculate the area of the triangle.
To calculate square root use:
```
import math
x = math.sqrt(10)
"""
import math

a = float(input('Insert the length of the side a of a triangle (in cm): '))
b = float(input('Insert the length of the side b of a triangle (in cm): '))
c = float(input('Insert the length of the side c of a triangle (in cm): '))

if a + b > c and a + c > b and b + c > a:
    s = 1 / 2 * (a + b + c)
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    print(f'The area of your triangle is {area:.2f}')

else:
    print("I'm sorry. You can't create a triangle from these lengths. The sum of any 2 sides has to be bigger than the 3rd side")