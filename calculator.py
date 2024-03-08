class Calculator:

    def sum (self, a, b):
        return a + b

    def sust (self, a, b):
        return a - b

    def mult (self, a, b):
        return a * b

    def div (self, a, b):
        return a / b


calc = Calculator()

x = calc.sum(2,4)
print(type(x), x)

y = calc.mult(2.5, 4)
print(type(y), y)

print(type(Calculator))

print(type(calc))
