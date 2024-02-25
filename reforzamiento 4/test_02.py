def error_en_lista(lista, indice):
    try:
        elemento = lista[indice]
        return elemento
    except IndexError:
        print("Error: No existe un elemento dentro de ese índice.")
        print("Por favor ingrese un índice válido.")
    except Exception as e:
        print("Error:", e)
        print("No se pudo completar la operación, surgió un error.")

lista = [2, 6, 10, 4, 5, 23, 1]
resultado = error_en_lista(lista, 10)
if resultado != None:
    print(f"El elemento de su índice es: {resultado}")
