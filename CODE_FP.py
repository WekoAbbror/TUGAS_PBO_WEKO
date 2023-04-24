# Program untuk menghitung luas lingkaran menggunakan FP
from math import pi

def calculate_area(r):
    return pi * r ** 2

radius = 5
area = calculate_area(radius)
print("Luas lingkaran dengan radius", radius, "adalah", area)
