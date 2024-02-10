class numero:
    def __init__(self):
        self.resultado = 0

    def numero_usuario(self):
        numero = int(input("Ingrese un número: "))
        return numero

    def cubo(self, numero):
        self.resultado = numero ** 3
        return self.resultado

    def cuadrado_cubo(self):
        resultado_cuadrado = self.resultado ** 2
        return resultado_cuadrado

operaciones = numero()
numero_ingresado = operaciones.numero_usuario()
cubo = operaciones.cubo(numero_ingresado)
cuadrado_cubo = operaciones.cuadrado_cubo()

print("El cubo del número ingresado es: ",cubo)
print("El cuadrado del cubo del número ingresado es: ",cuadrado_cubo)

