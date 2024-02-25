def decorador(funcion):
    def wrapper(*args, **kwargs):
        print("¡Buenos días!")
        resultado = funcion(*args, **kwargs)
        print("Hasta luego")
        return resultado
    return wrapper

@decorador
def funcion_a_decorar(nombre):
    return f"Soy {nombre}"


nombre = input("Ingrese su nombre: ")
mensajito = funcion_a_decorar(nombre)
print(mensajito)