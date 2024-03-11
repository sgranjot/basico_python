from calculator import Calculator
class Estudiante:

    num_students=0

    def __init__(self, nombre, edad, curso):
        self.nombre = nombre
        self.edad = edad
        self.curso = curso
        Estudiante.num_students +=1

    def estudianteSuma(self, calculator, a, b):
        return self.nombre + ' sumando ' + (str)(a) + '+' + (str)(b) + '=' + (str)(calculator.sum(a, b))

print('vemos como aumenta el atributo de clase con la creacion de estudiantes:')
est_1 = Estudiante('Pepe', 40, 'Python')
print(est_1.nombre, est_1.num_students)
est_2 = Estudiante('Paco', 33, 'Java')
print(est_2.nombre, est_2.num_students)
est_3 = Estudiante('Maria', 27, 'JavaScript')
print(est_3.nombre, est_3.num_students)
est_4 = Estudiante('Ana', 29, 'Angular')
print(est_4.nombre, est_4.num_students)

estudiantes = [est_1, est_2, est_3, est_4]

for estudiante in estudiantes:
    print(estudiante.nombre, estudiante.edad, estudiante.curso)

calc = Calculator()

print(est_1.estudianteSuma(calc,3,2))

