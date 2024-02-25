def agregar_usuario(nombre, apellido, edad):

    with open("agenda_test10.txt", "a") as archivo:
        archivo.write(f"{nombre},{apellido},{edad}\n")


nombre = input("Introduce el nombre del usuario: ")
apellido = input("Introduce el apellido del usuario: ")
edad = input("Introduce la edad del usuario: ")

agregar_usuario(nombre, apellido, edad)