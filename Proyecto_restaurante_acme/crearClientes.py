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
        
    
        datos_cliente = {
            "Identificacion" : identificaion,
            "Nombre" : nombre,
            "Telefono" : telefono,
            "Email" : email
        }
        
        try:
            with open("Clientes.json", "r") as clientes:
                lista_clientes = json.load(clientes)
        except (FileNotFoundError, json.JSONDecodeError):
            lista_clientes = []
            
        lista_clientes.append(datos_cliente)
        
        with open("Clientes.json", "w") as archivo:
            json.dump(lista_clientes, archivo)
            
        print("Cliente guardado exitosamente")
        
    except ValueError:
        print("Ingrese un dato valido")
        
        
    print(decoracion)