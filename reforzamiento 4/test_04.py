def error_entre_cero(string, divisor):
    try:
        result = string / divisor
        return result
    except ZeroDivisionError:
        print("ERROR: No se puede dividir un string, asegurarse que el divisor no sea cero")
    except TypeError:
        print("ERROR: No se puede dividir, revisar que sea entre números naturales")
        print("Revisar si se está dividiendo entre números")
    except Exception as e:
        print("ERROR:", e)
        print("No se pudo completar la operación debido a un error.")

string = "Hello Pythonista"
result = error_entre_cero(string, 0)