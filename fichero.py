# Escribir
file = open('prueba.txt', 'w')
file.write('Esto es una línea\n')
file.close()


# Leer
file = open('prueba.txt', 'r')
line = file.read()
print(line)
file.close()

