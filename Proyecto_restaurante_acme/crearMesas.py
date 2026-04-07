import json


def crearMesas():
    decoracion = "=" * 50
    print(decoracion)
    print("Modulo de crear mesas")
    
    try:
        codigo = int(input("Ingrese el codigo de la mesa : "))
        nombre = input("Ingrese el nombre de la mesa : ")
        puestos = int(input("¿cuantos puestos tiene esta mesa? : "))
        
    except ValueError:
        print("Ingrese un dato valido")
        
        
    datos_mesas = {
        "Codigo" : codigo,
        "Nombre" : nombre,
        "Puestos" : puestos
    }
    
    with open("Mesas.json", "w") as archivo:
        json.dump(datos_mesas, archivo)
    

        
    print(decoracion)   