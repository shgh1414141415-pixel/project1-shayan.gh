
import sys
import math

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))
if a == 0:
    print("Error: a must not be zero")

else:
    delta = b*b - 4.0*a*c

    if delta > 0:
        root = math.sqrt(delta)
        print((-b + root)/(2*a))
        print((-b - root)/(2*a))

    elif delta == 0:
        print(-b/(2*a))

    else:
        print("No real roots")
