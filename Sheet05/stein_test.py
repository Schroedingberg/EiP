import math
import itertools
import stein
# values = "7 \n1005 n\n18 12\n3528 3780\n144 160\n16 175\n0 17\n17 0"

# valuelist = values.split("\n")
# n = int(valuelist[0])+1
# ABs = [[int(i) for i in AB.split(" ")]for AB in valuelist[1:]]

# results = [int(stein.stein_rec(zahlenpaar[0], zahlenpaar[1])) for
#            zahlenpaar in ABs]

# expected = [5, 6, 252, 16, 1, 17, 17]
# print("My results: {0}".format(results))
# print("Expected: {0}".format(expected))
# if results == expected:
#     print("Sauce test pass")

import time
import matplotlib.pyplot as plt
myalgtimes = []
benchmark = []
for a in range(100):
    ValPairs = itertools.combinations(range(a), 2)
    start = time.time()
    my_alg = [stein.stein_rec(i[0], i[1], 0) for i in ValPairs]
    end = time.time()
    myalgtimes.append(end-start)
for a in range(100):
    ValPairs = itertools.combinations(range(a), 2)
    start = time.time()
    correct = [math.gcd(i[0], i[1]) for i in ValPairs]
    end = time.time()
    benchmark.append(end-start)

# fig = plt.figure()
# ax = fig.add_subplot(111)
# ax.plot(range(100), myalgtimes, label="Unsere rekursive Implementierung ")
# ax.plot(range(100), benchmark, label="ggT aus python's math Bibliothek")
# ax.legend()
# plt.show()
if my_alg == correct:
    print("Alrighty")
else:
    print("Own test fail")
