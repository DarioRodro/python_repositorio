lista = []
for i in range (1,30):
    if i %2 != 0:
        lista.append(i)
print(f"Los valores de los primeros 15 impares son: {lista}")
for e in range (1,4):
    lista.append(1.1)
print(f"Los valores de mi lista actualizada, agregando 3 numeros flotantes repetidos son: {lista}")
lista.insert(3, "Dariooo")
print(f"Los valores actualizados de mi lista, agregando una cadena en la posicion #3 de la lista son: {lista}")
del lista[3]
print(f"Los valores finales de mi lista, eliminando el valor en la posición #3 con la función 'del[]' son: {lista}")