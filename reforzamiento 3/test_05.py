
def funcion(lista,eliminar):
    if eliminar in lista:
        lista.remove(eliminar)
        print("Número eliminado: ", eliminar)
        print("Lista actualizada: ", lista)
    else:
        print("El número", eliminar, "no está en la lista")

var1 = int(input("Ingrese un valor: "))
var2 = int(input("Ingrese otro valor: "))
lista = []

n = int(input("Ingrese tamaño de su lista: "))
for i in range(n):
    elemento = int(input("Ingrese el elemento " + str(i+1) + " de la lista: "))
    lista.append(elemento)

    print("Lista original: ", lista)

    eliminar = int(input("Ingrese el valor que desee eliminar de la lista: "))

    funcion(lista, eliminar)

