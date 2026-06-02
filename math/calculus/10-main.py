#!/usr/bin/env python3

poly_derivative = __import__('10-matisse').poly_derivative

poly = [5, 3, 0, 1]
print(poly_derivative(poly))

print("---")

poly = []
print(poly_derivative(poly))
print("---")
poly = [4]
print(poly_derivative(poly))
print("---")
poly = [0]
print(poly_derivative(poly))

print("---")
poly = [5, 3, True, 1]
print(poly_derivative(poly))
print("---")
poly = [5, 'test', 0, 1]
print(poly_derivative(poly))
print("---")
poly = [5, 5, 3, 2, 1]
print(poly_derivative(poly))
print("---")
poly = [5, -3, 0, -1]
print(poly_derivative(poly))