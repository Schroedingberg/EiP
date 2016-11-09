# Variablen a und b werden gespeichert
a = 12
b = 4
# Ergebnisse verschiedener arithmetischer Operationen mit a und b werden in Variablen gespeichert
sum = a+b
division = a/b
intDivision = a//b
remainder = a % b
# Ausgabe der Ergebnisse im Format Operation: Ergebnis. Die 
# Variablen werden für die String-Concatenation nur als Rückgabewerte der Funktion str() eingesetzt.
# Strings mit Zahlen zu verketten ist nicht möglich.
print( "Summe:" + str(sum))
print("Quotient: " + str(division))
print("Ganzzahliger Quotient: " + str(intDivision))
print("Rest:" + str(remainder))

example_calculations = [sum, division, intDivision, remainder]
types = [type(calculation) for calculation in example_calculations]
print(types)


