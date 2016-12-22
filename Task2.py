import random
import math


def gaussian():
    """Generates gaussian random numbers, using a Box-Muller-formula based
    transformation on random point data in a unit circle."""
    r = 0.0
    while(r >= 1.0) or (r < 1e-10):
        x = -1.0 + 2.0 * random.random()
        y = -1.0 + 2.0 * random.random()
        r = x * x + y * y

    return x * math.sqrt(-2.0 * math.log(r) / r)


def nrandoms(n):
    return [gaussian() for i in range(n)]

arr = nrandoms(19)
print(len([0.05 * i for i in if]))
