
import random
# Initialize an integer counter variable that will represent the
# number of hits inside a circle.
Ncircle = 0
# Define a variable for the total amount of random experiments, for
# example 1 million in this case
Ntotal = 10**6
# Execute the random experiment "throw point in unit square" Ntotal times
for i in range(Ntotal):
    # Assign uniformly distributed random numbers between 0 and 1 to
    # variables x and y. This represents random points in the
    # two-dimensional plane.
    x = random.uniform(0, 1)
    y = random.uniform(0, 1)
    # Check whether the randomly chosen point lies within the quarter
    # unit circle using the Pythagorean theorem. If it does, increment Ncircle.
    if x**2+y**2 <= 1:
        Ncircle += 1

# Assign the approximated value for pi to the variable piapprox. The
# quotient of the circle-hits and the total number of throws is
# multiplied by four because the simulation models a quarter circle
# rather than a full circle.
piapprox = 4*(Ncircle/Ntotal)
print(piapprox)
