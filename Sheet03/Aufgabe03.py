import math
# Define a function that takes three coefficients a, b and c as arguments and
# returns the solutions for the second order polynomial containing these coefficients.
def solve(a, b, c):
    if b**2 >= 4*a*c: # This can be simplified to make the code more concise
        A = -b+math.sqrt((b**2)-4*a*c)
        B = 2*a
        return A/B
    else:
        print("Math error. Imaginary numbers not supported.")
# Implement second degree polynomial solver
a = 2
b = 6
c = 1
print(solve(a,b,c))
