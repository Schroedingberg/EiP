import math


def dragoncurve(n):
    if n == 0:
        return "F"
    if n == 1:
        return "RF" 
    else:
        head = dragoncurve(n - 1)
        m = len(head)
        tail = head[math.floor(m / 2) - 1] + "L" + head[math.floor(m / 2):-1]
        return dragoncurve(n - 1) + "R" + tail


def test(your_result,n):
    right = ["R",
             "RRL",
             "RRLRRLL",
             "RRLRRLLRRRLLRLL",
             "RRLRRLLRRRLLRLLRRRLRRLLLRRLLRLL", ]
    print(str(n)+your_result.replace("F",""))

for elem in range(5):
    test(dragoncurve(elem),elem)
