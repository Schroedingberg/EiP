import math


# Define a function that takes three coefficients a, b and c as arguments and
# returns a list of the solutions for the second (or lower) order polynomial containing
# these coefficients. It is assumed that the polynomial already has the
# standard form ax^2+bx+c = 0. If a is zero an error will be thrown, because
# division by zero is not allowed.
def solve(a, b, c):
    if b**2 >= 4*a*c: # Make sure that no negative numbers are in the discriminant.

        # The "plusminus" is implemented by defining two variables for the
        # dividend. One for the case of addition of the root-term, another one
        # for the subtraction of the root term.
        Aplus = -b+math.sqrt((b**2)-4*a*c)
        Aminus = -b-math.sqrt((b**2)-4*a*c)
        B = 2*a # The divisor of the given formula
        return [Aplus/B, Aminus/B]
    else:
        print("Error. You entered coefficents that that require the computation of the square root of a negative number. This would require to extend the domain to imaginary numbers which is not supported.")

a = int(input("Please enter a value for a (The coefficient of x^2):"))
b = int(input("Please enter a value for b (The coefficient of x):"))
c = int(input("Please enter a value for c (The coefficient of 1):"))
print(solve(a, b, c))
