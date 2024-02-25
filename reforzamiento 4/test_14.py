def decorador(funcion):
    def wrapper(*args, **kwargs):
        print("La cantidad de argumentos que tiene la función es:")
        print(len(args) + len(kwargs))
        resultado = funcion(*args, **kwargs)
        print("La función decoradora terminó de ejecutarse correctamente")
        return resultado
    return wrapper

@decorador
def suma(*args):
    return sum(args)


resultado = suma(5, 19, 54, 1, 5, 49)
print("El resultado de la suma es:", resultado)
