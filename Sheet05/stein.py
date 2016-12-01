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
    argument.
    """

    if A == 0:
        print("A==0")
        return B*2**k
    if B == 0:
        print("B==0")
        return A*2**k
    if even(A) and even(B):
        print("A and B even")
        return stein_rec(A/2, B/2, k+1)
    if even(A) and not even(B):
        print("A even, B not")
        return stein_rec(A/2, B, k)
    if even(B) and not even(A):
        print("B even not A")
        return stein_rec(A, B/2, k)
    elif A >= B:
        print("A >= B")
        return stein_rec((A-B)/2, B, k)
    elif B > A:
        print("B> A")
        return stein_rec(A, (B-A)/2, k)

if __name__ == "__main__":
    valuelist = [3528, 3780]
    print(stein_rec(valuelist[0], valuelist[1]))
