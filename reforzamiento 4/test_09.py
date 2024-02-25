def tabla_multi(numero):
    if numero < 1 or numero > 20:
        print("El número debe estar entre 1 y 20.")
        return

    with open("tabla.txt", "w") as archivo:
        archivo.write(f"Esta es la abla de multiplicar del {numero}:\n")
        for i in range(1, 11):
            resultado = numero * i
            archivo.write(f"{numero} x {i} = {resultado}\n")


numero_usuario = int(input("Introduce un número entero entre 1 y 20: "))
tabla_multi(numero_usuario)