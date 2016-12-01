n = 9
def collatz_iterative(n):
    x = n
    seq = []
    while x != 1:
        if x % 2 == 0:
            x = x/2
            seq.append(x)
        else:
            x = 3*x+1
            seq.append(x)
    return seq


def collatz_recursive(n):
    if n == 1:
        return [1]
    elif n % 2 == 0:
        return [collatz_recursive(n/2)] 
    else:
        return [collatz_recursive(3*n+1)]
