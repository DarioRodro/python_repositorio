def decorador(funcion):
    def wrapper(*args, **kwargs):
        print("Está por ejecutarse la función")
        resultado = funcion(*args, **kwargs)
        print("La función ha sido ejecutada correctamente")
        return resultado
    return wrapper

@decorador
def multiplica(*args):
    resultado = 1
    for num in args:
        resultado *= num
    return resultado

resultado = multiplica(6, 7, 8, 9)
print("El resultado de la multiplicación es:", resultado)