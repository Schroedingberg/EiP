import matplotlib.pyplot as plt
import math
# Render any text in plots with LaTeX
from matplotlib import rc
rc('text', usetex=True)


# Define a dictionary of functions with their names as indices.
functions = {"log_2(n)": lambda x: math.log2(x),
             "n": lambda x: x,
             "ln(n)": lambda x: x * math.log(x),
             "n^2": lambda x: x**2,
             "n^3": lambda x: x**3,
             "2^n": lambda x: 2**x}
# Define the range n = 2, ..., 12 as input for the example functions
# as requested in the task.
n = range(2, 14, 2)
# Calculate a dictionary of lists of values for each function in the
# function dictionary. The keys are the same keys used in the function
# dictionary. This will make the generation of a legend more
# convenient and concise.
values = {key: [functions[key](i) for i in n] for key in functions.keys()}
# Plot the n-values against their corresponding function values, using
# the dictionary keys as labels for each plot. The $ that are added to
# the key are LaTeX-math delimiters. This has the effect that the
# function names will be rendered nicely.
for key in values.keys():
    plt.plot(n, values[key], label="$" + key + "$")
# Generate the legend for the generated plot. The argument loc = 0 is
# provided to avoid the legend to cover the lines.
plt.legend(loc=0)
# Save the plot to a file.
plt.savefig("plot1.png")
# Delete the plot object to avoid errors when generating the next plot.
plt.close()
# Repeat the same plotting process, but this time use a logarithmic
# y-axis.
for key in values.keys():
    plt.semilogy(n, values[key], label="$" + key + "$")
plt.legend(loc=0)
plt.savefig("plot2.png")
plt.close()
