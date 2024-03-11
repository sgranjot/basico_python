def sum (a,b):
    return a+b

def rest (a,b):
    return a-b

operaciones = [sum, rest]

suma= operaciones[0]
print('la suma es:', suma(3,2))

resta = operaciones[1]
print('la resta es:', resta(3,2))