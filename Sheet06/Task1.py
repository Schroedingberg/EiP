import random
import statistics


def basic_stats_builtin(x):
    """Return simple statistics about an array as a dictionary, using
    builtin functions and the statistics module for the mean.

    """
    return {"Minimum: ": min(x), "Maximum: ": max(x), "Sum: ": sum(x),
            "Mean: ": statistics.mean(x)}


def basic_stats_custom(x):
    """Return simple statistics about an array as a dictionary, using
    own defined functions.
    """
    def my_min(x):
        m = x[0]
        for elem in x:
            if elem < m:
                m = elem
            else:
                pass
        return m

    def my_max(x):
        m = x[0]
        for elem in x:
            if elem > m:
                m = elem
            else:
                pass
        return m

    def my_sum(x):
        acc = 0
        for elem in x:
            acc += elem
        return acc

    def my_len(x):
        acc = 0
        for elem in x:
            acc += 1
        return acc

    def my_mean(x):
        """Return the mean of numbers in list. Since the task is not to use
        builtin functions, length is also defined anew (prior to this
        function definition).

        """
        return my_sum(x) / my_len(x)
    return {"Minimum: ": my_min(x), "Maximum: ": my_max(x), "Sum: ":
            my_sum(x), "Mean: ": my_mean(x)}

# Assumption: Random numbers in the task refer to unifiedly
# distributed random numbers
x = [random.uniform(0, 1000) for i in range(100)]
# Assign return values of the basic statistics functions with x as
# argument to variables to allow for easy iteration. Then iterate through
# both dictionaries by their keys, pretty-printing the key value
# pairs. Pretty-printing includes rounding to two digits.
builtin = basic_stats_builtin(x)
print("Calculating basic statistics about the array using builtin functions...")
for name in builtin.keys():
    print(name + str(round(builtin[name], 2)))

print("Calculating basic statistics about the array using custom functions...")
custom = basic_stats_custom(x)
for name in custom.keys():
    print(name + str(round(custom[name], 2)))
