"""test 19"""

lista = []
print(f"Esta lista está vacia {lista}")
for i in range(1, 11):
    lista.append(float(input(f"Ingrese el valor #{i} para la lista_9:")))
print(f"Los valores de mi lista_9 son: {lista}")
suma_elementos = sum(lista)
print(f"La suma de los elementos de mi lista es: {suma_elementos} ")
media_elementos = suma_elementos/i
print(f"La media de los elementos de mi lista es: {media_elementos}")