from calculator import Calculator
class Estudiante:

    def __init__(self, nombre, edad, curso):
        self.nombre = nombre
        self.edad = edad
        self.curso = curso

    def estudianteSuma(self, calculator, a, b):
        return self.nombre + ' sumando ' + (str)(a) + '+' + (str)(b) + '=' + (str)(calculator.sum(a, b))

est_1 = Estudiante('Pepe', 40, 'Python')
est_2 = Estudiante('Paco', 33, 'Java')
est_3 = Estudiante('Maria', 27, 'JavaScript')
est_4 = Estudiante('Ana', 29, 'Angular')

estudiantes = [est_1, est_2, est_3, est_4]

for estudiante in estudiantes:
    print(estudiante.nombre, estudiante.edad, estudiante.curso)

calc = Calculator()

print(est_1.estudianteSuma(calc,3,2))