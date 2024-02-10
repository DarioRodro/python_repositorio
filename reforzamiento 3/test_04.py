def num_palabras(oracion):
    #Split dividira la oracion en una lista de palabras
    palabras = oracion.split()

    cantidad_palabras = len(palabras)
    return cantidad_palabras

oracion_insertada = input("Introduce una oracion como mínimo de tres palabras: ")

while num_palabras(oracion_insertada) < 3:
    print("La oracion no tiene la suficiente cantidad de palabras.")
    oracion_insertada = input("Introduce una oracion como mínimmo de tres palabras: ")

numero_palabras = num_palabras(oracion_insertada)

print(f"La oracion ingresada tiene {numero_palabras} palabras.")