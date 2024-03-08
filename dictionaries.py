dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
dict2 = {'e': 5, 'f': 6, 'g': 7, 'h': 8}

dict3 = {**dict1, **dict2}


#imprimir diccionario:
print(dict3)

# recorrer diccionario clave-valor:
for key, value in dict3.items():
    print(key, ':', value)

# imprimir claves:
print(dict3.keys())

# recorrer claves:
for key in dict3:
    print(key)

# imprimir valores:
print(dict3.values())

# recorrer valores:
for value in dict3.values():
    print(value)




