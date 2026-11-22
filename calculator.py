# https://github.com/calevzak/lab11-CZ-MH.git
# Partner 1: Calev Zak
# Partner 2: Mitchel Horkheimer
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
    if a == 0:
        raise ZeroDivisionError("division by zero")
    return b/a

def exp(a, b):
    return a**b

def square_root(a):
    if a < 0:
        raise ValueError("square root")
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def logarithm(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError("logarithm")
    return math.log(b, a)