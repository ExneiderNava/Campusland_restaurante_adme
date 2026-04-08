import json


def crearMesas():
    decoracion = "=" * 50
    print(decoracion)
    print("Modulo de crear mesas")
    
    try:
        codigo = int(input("Ingrese el codigo de la mesa : "))
        nombre = input("Ingrese el nombre de la mesa : ")
        puestos = int(input("¿cuantos puestos tiene esta mesa? : "))
        
        datos_mesas = {
            "Codigo" : codigo,
            "Nombre" : nombre,
            "Puestos" : puestos
        }
        
        try:
        
            with open("Mesas.json", "r") as archivo:
                lista_mesas = json.load(archivo)
        except (FileNotFoundError, json.JSONDecodeError):
            lista_mesas = []
            
        lista_mesas.append(datos_mesas)
        
        with open("Mesas.json", "w") as archivo:
                json.dump(lista_mesas, archivo)
                
        print("Mesa guardada")
        
    except ValueError:
        print("Ingrese un dato valido")
    

        
    print(decoracion)   