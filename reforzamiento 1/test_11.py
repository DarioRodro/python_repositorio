"""TEST 11"""

num = int(input("Introduce un número: "))

resultado = pow(num, 5) /10

resultado_int = int(resultado) if resultado.is_integer() else resultado
print(f"el resultado de este numero elevado en 5 y dividido entre 10 es {resultado_int}")
print("el tipo de dato del resultado es ", type(resultado_int))