lista = ["calculo I", "lenguaje", "fundamentos de números", "geometría vectorial", "programacion", " introduccion al algebra"]

list.append(lista, "Aritmetica")
list.append(lista, "Aritmetica")
list.append(lista, "Programacion")

print(f"La nueva lista es: {lista}")

print("El curso de aritmetica se repite: {}".format(lista.count("Aritmetica")))
