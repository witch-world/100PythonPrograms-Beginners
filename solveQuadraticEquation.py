# cmath library --> complexmath library

import cmath
a = int(input("Enter a (a != 0): "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

# calculating discriminant
dis = (b ** 2) - (4 * a * c)

# finding roots
root1 = (-b-cmath.sqrt(dis))/(2*a)
root2 = (-b+cmath.sqrt(dis))/(2*a)

print(f"\nResults for equation {a}x**2 + {b}x + {c} = 0 are: \n")

if dis > 0:
    print("Type of Roots: Two Distinct Real Roots")
elif dis == 0:
    print("Type of Roots: Two Equal Real Roots")
else:
    print("Type of Roots: Two Complex Roots")

print(f"The Roots are {root1} and {root2}")