
import json



def crearProductos():
   
    decoracion = "=" * 50
 
    print(decoracion)
    print("Modulo de ingresar producto")
    
    try:
        codigo = int(input("Ingrese el codigo del producto: ")) 
        nombre = input("Ingrese el nombre del producto: ")
        valor_unitario = int(input("Ingrese el valor unitario de ese producto: "))
        iva = int(input("Ingrese el IVA de este producto: "))
        
    except ValueError:
        print("Por favor ingrese algo valido")
    
    datos_producto = {
        "codigo" : codigo,
        "Nombre" : nombre ,
        "Valor Unitario" : valor_unitario,
        "Iva" : iva
    }
    
    with open("productos.json", "w") as archivo:
        json.dump(datos_producto, archivo)
    
    print(decoracion)