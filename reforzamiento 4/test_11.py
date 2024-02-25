def guardar_calificacion(nombre, nota1, nota2):
    promedio = (nota1 + nota2) / 2

    with open("calificaciones_test11.txt", "a") as archivo:
        archivo.write(f"{nombre},{nota1},{nota2},{promedio}\n")


def verificar_aprobacion(nombre_alumno):
    with open("calificaciones.txt", "r") as archivo:
        lineas = archivo.readlines()
        for linea in lineas:
            partes = linea.strip().split(",")
            nombre = partes[0]
            promedio = float(partes[3])
            if nombre == nombre_alumno:
                if promedio >= 10:
                    return f"El alumno {nombre_alumno}, aprobado"
                else:
                    return f"El alumno {nombre_alumno}, desaprobado"
        return "Alumno no encontrado"


guardar_calificacion("Dario", 15, 18)
guardar_calificacion("Sebastian", 8, 12)
guardar_calificacion("Estefani", 10, 11)

print(verificar_aprobacion("Dario"))
print(verificar_aprobacion("Sebastian"))
print(verificar_aprobacion("Messi"))