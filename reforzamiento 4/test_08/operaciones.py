import math
def insertar_entero():
    try:
        valor = int(input("Introduce un número entero: "))
        return valor
    except ValueError:
        print("ERROR: Introduce un número entero")
        return None

def raiz_cuadrada(valor):
    if valor is not None:
        raiz_cuadrao = math.sqrt(valor)
        print(f"La raíz cuadrada de {valor} es: {raiz_cuadrao}")

def cuadrao_cubo(valor):
    if valor is not None:
        cuadrao = pow(valor, 2)
        cubo = pow(valor, 3)
        print(f"El valor de su número {valor} al cuadrado es: {cuadrao}")
        print(f"El valor de de su número {valor} al cubo es: {cubo}")