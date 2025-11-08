import math

def circle_properties(radius):
    """Calculate the area and circumference of a circle given its radius."""
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return area, circumference


def factorial(n):
    """Calculate the factorial of a number."""
    if n < 0:
        return "Factorial not defined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        fact = 1
        for i in range(1, n + 1):
            fact *= i
        return fact
