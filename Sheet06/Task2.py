n = int(input())
A = []
for i in range(n):
    A.append(int(input()))
x = int(input())


def horner(A, x):
    """Return the solution of a polynomial with the coefficients A at the
    given value x.
    """
    b = 0
    for a in A:
        b = b * x + a
    return bn


print(horner(A, x))
