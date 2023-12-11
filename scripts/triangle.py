import math

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

if (a + b > c) and a + c > b and b + c > a:
    perimeter = a + b + c
    s = perimeter * 0.5
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    print(f"perimeter is {perimeter:.2f}")
    print(f"area is {area:.2f}")
else:
    print("Cannot form a triangle")
