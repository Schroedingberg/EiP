import math
import itertools
from stein import *
values = "7 \n1005 25\n18 12\n3528 3780\n144 160\n16 175\n0 17\n17 0"

valuelist = values.split("\n")
n = int(valuelist[0])+1
ABs = [[int(i) for i in AB.split(" ")]for AB in valuelist[1:]]
for zahlenpaar in ABs:
    print(stein_rec(zahlenpaar[0], zahlenpaar[1], 0))


ValPairs = itertools.combinations(range(20), 2)

my_alg = [stein_rec(i[0], i[1]) for i in ValPairs]
correct = [math.gcd(i[0], i[1]) for i in ValPairs]
if my_alg == correct:
    print("Alrighty")
else:
    print("Fail")
