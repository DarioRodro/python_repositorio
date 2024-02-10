
num1 = int(input("Ingrese el primer numero: "))

while (num1 <= 0):
    num1 = int(input("Vuelva a ingregar el primer numero: "))

num2 = int(input("Ingrese el segundo numero"))

while (num2 <= 0):
    num2 = int(input("Vuelva a ingresar el segundo numero"))

def sumat_digitos(a):
    suma_digitos = 0
    a_string = str(a)
    for digitos in a_string:
        suma_digitos = suma_digitos + int(digitos)
    return suma_digitos

suma_digitos1 = sumat_digitos(num1)
suma_digitos2 = sumat_digitos(num2)


if suma_digitos1 > suma_digitos2:
    print(f"El número cuya sumatoria de dígitos es mayor es {suma_digitos1}")
elif suma_digitos2 > suma_digitos1:
    print(f"El número cuya sumatoria de dígitos es mayor es {suma_digitos2}")
else:
    print("La sumatoria de digitos de cada número son iguales")

if suma_digitos1 < 10:
    print(f"La sumatoria de dígitos del {suma_digitos1} es menor a 10")
if suma_digitos2 < 10:
    print(f"La sumatoria de dígitos del {suma_digitos2} es menor a 10")