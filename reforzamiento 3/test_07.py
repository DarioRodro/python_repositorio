
class revertir:
    def revertir_palabra(self, texto):
        palabra = texto.split()
        reversed_texto = ' '.join(reversed(palabra))
        return reversed_texto

revertirse = revertir()

input_texto = "Hola, Pythonista, seguimos adelante"
output_texto1 = revertirse.revertir_palabra(input_texto)
print("Resultado 1: ", output_texto1)

input_texto = "Hola, Dario, sigue adelante"
output_texto2 = revertirse.revertir_palabra(input_texto)
print("Resultado 2: ", output_texto2)


