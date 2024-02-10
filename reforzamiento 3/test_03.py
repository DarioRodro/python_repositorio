
num1 = int(input("Ingrese un número: "))

def sumat_digitos(a):
    suma_digitos = 0
    a_string = str
    for digitos in str(a):
        suma_digitos += int(digitos)
    return suma_digitos

print(f"La suma de dígitos de el número ingresado es: {sumat_digitos(num1)}")