import math

num = float(input("Enter the value: "))

if num > 0:
    print("Square Root is:", math.sqrt(num))
    print("Natural Logarithm (base e) is:", math.log(num))
else:
    print("Cannot compute square root or logarithm of non-positive numbers.")

print("Sine value (in radians) is:", math.sin(num))
