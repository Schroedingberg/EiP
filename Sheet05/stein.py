def even(x):
    """Helper function to check whether a given integer is even. Returns
    True if integer is even, False if not."""
    if x % 2 == 0:
        return True
    else:
        return False


def stein_rec(A, B, k=0):
    """Recursive implementation of Stein's Algorithm for calculating the
    greatest common divisor of two given integers.  The abort case is
    A or B being zero. In this case, the larger one of both i.e. the
    one that is not zero, multiplied with 2^k is returned, according
    to the given description of the algorithm.  k is provided as an
    argument, however
    """
    if A == 0:
        return int(B * 2**k)
    if B == 0:
        return A * 2**k
    if even(A) and even(B):
        return stein_rec(A / 2, B / 2, k + 1)
    if even(A) and not even(B):
        return stein_rec(A / 2, B, k)
    if even(B) and not even(A):
        return stein_rec(A, B / 2, k)
    elif A >= B:
        return stein_rec((A - B) / 2, B, k)
    elif B > A:
        return stein_rec(A, (B - A) / 2, k)
n = int(input())
values = []
for i in range(n):
    values.append([int(x) for x in input().split(" ")])
for elem in values:
    A, B = elem[0], elem[1]
    print(stein_rec(A, B))
