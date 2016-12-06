

def dragoncurve(n):
    if n == 0:
        return "F"
    if n == 1:
        return "FLF" 
    else:
        head = dragoncurve(n-1)
        tail = head.replace("L", "R")
        return


print(dragoncurve(2))
