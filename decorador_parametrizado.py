def mi_decorador (arg):
    def decorador_real(funcion):
        def nueva_funcion(a,b):
            print (arg)
            c = funcion (a,b)
            print(arg)
            return c
        return nueva_funcion
    return decorador_real

@mi_decorador("imprime esto antes y despues")
def suma(a,b):
    print("entra en funcion suma")
    return a +b

print (suma(5,8))