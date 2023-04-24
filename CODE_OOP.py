# Program untuk menghitung luas lingkaran menggunakan OOP
from math import pi

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return pi * self.radius ** 2

my_circle = Circle(5)
area = my_circle.calculate_area()
print("Luas lingkaran dengan radius", my_circle.radius, "adalah", area)
