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
    argument, however it is assigned the default value 0 so it is not
    necessary to explicitly pass it as an argument.

    """
    if A == 0 or B == 0:
        return [A, B]*2**k
    if even(A) and even(B):
        return stein_rec(A/2, B/2, k+1)
    if even(A):
        return stein_rec(A/2, B, k)
    if even(B):
        return stein_rec(A, B/2, k)
    elif A >= B:
        return stein_rec((A-B)/2, B, k)
    elif B > A:
        return stein_rec(A, (B-A)/2, k)






if __name__ == "__main__":
    
    values = "7 \n1005 25\n18 12\n3528 3780\n144 160\n16 175\n0 17\n17 0\n2854 705\n2855 705"

    valuelist = values.split("\n")
    n = int(valuelist[0])+1
    ABs = [[int(i) for i in AB.split(" ")]for AB in valuelist[1:]]
    for zahlenpaar in ABs:
        print(stein_rec(zahlenpaar[0], zahlenpaar[1], 0))





