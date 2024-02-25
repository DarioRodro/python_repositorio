def encontrar_error():
    try:
        var1 = int(input("Introduce tu dato: "))
        var2 = int(input("Introduce otro dato: "))
        suma = var1 + var2
        return suma
    except ValueError:
        print("Error: Solo se suma entre números o datos tipo int")
    except Exception:
        print("Error: Operación inconclusa debido a un error")
resultado = encontrar_error()

if resultado is not None:
    print(f"La suma de sus datos es: {resultado}")

