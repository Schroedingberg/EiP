# Set variables a and b
a = 12
b = 4
# Assign results of some arithmetic operations to variables.
sum = a+b
division = a/b
intDivision = a//b
remainder = a % b
# Print concatenation of words describing the results with the results cast to strings to STDOUT
print("Summe:" + str(sum))
print("Quotient: " + str(division))
print("Ganzzahliger Quotient: " + str(intDivision))
print("Rest:" + str(remainder))
# Create a list of the previously defined variables
example_calculations = [a, b ,sum, division, intDivision, remainder]
# Create a list containing the types of the elements in the previously defined list
types = [type(calculation) for calculation in example_calculations]
# Print the list "types" to STDOUT
print(types)
###
print("b = 4.0")
b = 4.0
sum = a+b
division = a/b
intDivision = a//b
remainder = a % b
print( "Summe:" + str(sum))
print("Quotient: " + str(division))
print("Ganzzahliger Quotient: " + str(intDivision))
print("Rest:" + str(remainder))
example_calculations = [a, b, sum, division, intDivision, remainder]
types = [type(calculation) for calculation in example_calculations]
print(types)
# Assigning 4.0 to b (which makes b a float), makes the results of the arithmetic operations floats as well.








