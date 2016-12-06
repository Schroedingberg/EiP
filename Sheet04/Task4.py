n = int(input())
# Define a range from 1 to n
r = range(1,n)
# Initialize an empty list to accumulate results 
cubesums = []
# Loop through possible combinations of numbers a,b,c,d to find cube sums that can be expressed in two ways.
# The ranges of iteration are narrowed down in the nested for loops to avoid redundant calculations.
for a in r:
        for b in range(a):
                # Make sure that only the Ramanujan numbers until n are
                # calculated. So if the counter variables exceed n, the loop is stopped.
                if a**3+b**3 >= n: break
                for c in range(a):
                        for d in range(c):
                                # DeMorgan's law is used to make this conditional concise
                                if not (a == b or a == c or a == d or  b == c or b == d or  c == d):
                                        # Compute the cube-sum of A and B and C and D
                                        AB = a**3+b**3
                                        CD = c**3+d**3
                                        if AB == CD:
                                                print(AB)
                                
        
                                

