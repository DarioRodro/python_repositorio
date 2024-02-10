
def cuadrados_entre_numeros(num1, num2):

    if num1 > num2:
        num1, num2 = num2, num1

    for i in range(num1 + 1 , num2):
        print(f"El cuadrado de {i} es: {i ** 2}")

numero1 = int(input('Ingrese un numero: '))

numero2 = int(input('Ingrese otro numero: '))

cuadrados_entre_numeros(numero1,numero2)