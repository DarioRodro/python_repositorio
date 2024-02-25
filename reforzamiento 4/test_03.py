def error_en_dict(persona):
    try:
        profesion = persona['profesion']
        return profesion
    except KeyError:
        print("Error: La llave 'profesion' no se encuentra en el diccionario")
        print("Verificar si la llave 'profesion' está en su diccionario")
    except Exception as e:
        print("Error: ", e)
        print("No se pudo completar la operación debido a un error.")

persona = {'nombre': 'Xavier', 'apellido': 'Rodriguez', 'dni': '7654321'}

resultado = error_en_dict(persona)
if resultado != None:
    print(f"La profesion es: {resultado}")