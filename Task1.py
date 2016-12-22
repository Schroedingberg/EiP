def invert_row(m):
    """Returns a list of booleans, containing the negations of all the
    elements in the input list. The input list has to be a list of
    booleans too.

    """
    return list(map(lambda x: not x, m))


def print_hadamard(h_n):
    """Prints a given matrix. According to the context of the function, it
    is called "print_hadamard", although it technically could print
    any matrix.  The formatting is implemented by casting the elements
    of each row to str and join them with whitespace as separator.

    """
    print("Hadamard of order: " + str(len(h_n)))
    for row in h_n:
        print(" ".join([str(i) for i in row]))


def generate_hadamard(h_n):
    """Returns hadamard matrix of twice the degree of the input matrix.
    The input matrix needs to be represented as a list of lists.
    The result is returned as a list of lists."""
    n = len(h_n)
    h_2n = [h_n[i % n] * 2 for i in range(2 * n)]
    for j in range(n):
        h_2n[n + j][n:] = invert_row(h_2n[n + j][n:])
    return h_2n


def get_all_hadamard_matrices(z):
    """Prints all hadamard matrices until order n = 2**z.
    """
    base = [[True]]  # The base case, H_1
    print_hadamard(base)
    for i in range(z):
        # Generate the base for the next Hadamard matrix from the Hadamard
        # matrix of previous order, until z
        base = generate_hadamard(base)
        print_hadamard(base)


n = int(input())
get_all_hadamard_matrices(n)
