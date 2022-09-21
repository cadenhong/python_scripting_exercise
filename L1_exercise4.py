'''
Area of a Triangle

Write a function that takes the base and height of a triangle and return its area.

Examples
tri_area(3, 2) ➞ 3
tri_area(7, 4) ➞ 14
tri_area(10, 10) ➞ 50

Notes
The area of a triangle is: (base * height) / 2
Don't forget to return the result.
'''

def tri_area(base, height):
    return (base * height)/2

print(tri_area(3, 2))
print(tri_area(7, 4))
print(tri_area(10, 10))
