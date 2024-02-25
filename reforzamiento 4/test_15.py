import urllib.request
import json

url = "https://jsonplaceholder.typicode.com/users"
response = urllib.request.urlopen(url)
data = json.loads(response.read())

for user in data:
    nombre = user["name"].split()[0]
    apellido = user["name"].split()[1]
    email = user["email"]
    nombreCompañia = user["company"]["name"]
    direccion = user["address"]["street"]
    nombreWeb = user["website"]

    # Mensaje
    oracion = f"Bienvenido {nombre} {apellido}, su correo electrónico es {email}. Usted trabaja en la compañía llamada {nombreCompañia}. Vive en {direccion}. Su sitio web es: {nombreWeb}"

    print(oracion)

nuevo_usuario = {
    "name": "Nuevo Usuario",
    "email": "nuevo@usuario.com",
    "company": {
        "name": "Nueva Compañía"
    },
    "address": {
        "street": "Calle Nueva 123"
    },
    "website": "www.nuevousuario.com"
}

data.append(nuevo_usuario)

print(data[-1])