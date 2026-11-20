"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
import math

def mul(a, b):
    return a*b

def div(a, b):
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return a/b

def exp(a, b):
    return a**b

def square_root(a):
    if a < 0:
        raise ValueError("square root")
    return math.sqrt(a)

def hypotenuse(a, b):
    if a == 0 or b == 0:
        raise ValueError("hypotenuse")
    return math.hypot(a, b)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def logarithm(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError("logarithm")
    return math.log(b, a)