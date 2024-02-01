"""DICCIONARIO 5"""

empleado = { "nombre": "Dario", "edad": 20, "salario": 1200, "edad para empleado": 20 }
empleado["dni"] = 74165766
del empleado["edad"]
lista = list(empleado)
print(f"Mi diccionario convertido es el siguiente: {lista}")
print(type(lista))