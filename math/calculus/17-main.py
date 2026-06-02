#!/usr/bin/env python3

poly_integral = __import__('17-integrate').poly_integral

poly = [5, 3, 0, 1]
print(poly_integral(poly))


print("---")

poly = []
print(poly_integral(poly))
print("---")
poly = [4]
print(poly_integral(poly))
print("---")
poly = [0]
print(poly_integral(poly))

print("---")
poly = [5, 3, True, 1]
print(poly_integral(poly))
print("---")
poly = [5, 'test', 0, 1]
print(poly_integral(poly))
print("---")
poly = [5, 5, 3, 2, 1]
print(poly_integral(poly, 5))
print("---")
poly = [5, -3, 0, -1]
print(poly_integral(poly, 33))

poly = [5, 3, 0, 1]
print(poly_integral(poly, True))