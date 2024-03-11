# Escribir
file = open('prueba.txt', 'w')
file.write('Esto es una línea\n')
file.close()

# si ponemos with open('prueba.txt, 'w') as file no seria necesario poner el file.close()


# Leer
file = open('prueba.txt', 'r')
line = file.read()
print(line)
file.close()


