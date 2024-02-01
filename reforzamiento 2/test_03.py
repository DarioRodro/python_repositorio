"""TEST 01"""

lista = ["calculo I", "lenguaje", "fundamentos de números", "geometría vectorial", "programacion", " introduccion al algebra"]

print(f"mi lista contiene estos cursos: {lista}")

"""TEST 02"""

list.append(lista, "Aritmerica")
list.append(lista, "Programacion")
list.append(lista, "Física")
list.append(lista, "Química")

print(f"Mi nueva lista contiene estos cursos: {lista}")

"""TEST 03"""

list.remove(lista, "Aritmerica")
list.remove(lista, "Programacion")

print(f"Al quitar 2 elementos de mi lista, ahora mi lista contiene: {lista}")