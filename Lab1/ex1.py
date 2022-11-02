from math import sqrt

print("Please enter a, b, c:")
a = int(input())
b = int(input())
c = int(input())
delta = b**2 - 4 * a * c
if delta < 0:
    print("No solution")
elif delta == 0:
    print(f"x = {-b/(2*a)}")
else:
    print(f"x1 = {(-b + sqrt(delta))/(2*a)}")
    print(f"x2 = {(-b - sqrt(delta))/(2*a)}")
