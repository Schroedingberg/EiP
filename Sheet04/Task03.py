import math
n = 2048
result = []
functions = [lambda x: math.log2(x), lambda x: x, lambda x: x*math.log(x), lambda x: x**2, lambda x: x**3, lambda x: 2**x]
for x in range(1,12):
    intermediate_result = []
    for fun in functions:
        intermediate_result.append(fun(2**x))
    result.append(intermediate_result)


for line in result:
    zeile = [str(i)+"\t" for i in line]
    print("".join(zeile))
