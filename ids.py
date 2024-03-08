import calculator

calc_1 = calculator.Calculator()
calc_2 = calculator.Calculator()
calc_3 = calc_2

if id(calc_2) == id(calc_3):
    print ('true')
else:
    print('false')

