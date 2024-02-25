import validar_usuario

nombre_usuario = input("Ingrese su nombre de usuario: ")

resultado = validar_usuario.validar_nombre(nombre_usuario)

if resultado is True:
    print("El nombre de usuario es válido.")
else:
    print(resultado)