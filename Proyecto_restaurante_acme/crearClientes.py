import json


def crearClientes():
    decoracion = "=" * 50
    print(decoracion)
    print("Modulo de Crear Clientes")
    try:
        identificaion = int(input("Ingrese el numero de identificacion: "))
        nombre = input("Ingrese el nombre: ")
        telefono = input("Ingrese el numero de telefono: ")
        email = input("Ingrese el Email: ")
        
    except ValueError:
        print("Ingrese un dato valido")
        
    datos_cliente = {
        "Identificacion" : identificaion,
        "Nombre" : nombre,
        "Telefono" : telefono,
        "Email" : email
    }
    
    with open("Clientes.json", "w") as archivo:
        json.dump(datos_cliente, archivo)
    
        
    print(decoracion)