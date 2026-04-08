
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
        
   
    
        datos_producto = {
            "codigo" : codigo,
            "Nombre" : nombre ,
            "Valor Unitario" : valor_unitario,
            "Iva" : iva
        }
        
        try:
            with open("productos.json", "r") as productos:
                
                lista_productos = json.load(productos)
                
        except (FileNotFoundError, json.JSONDecodeError):
            
            lista_productos = []
            
        lista_productos.append(datos_producto)
            
        
        with open("productos.json", "w") as archivo:
            json.dump(lista_productos, archivo)
        
        print("Producto guardado exitosamente")
            
    except ValueError:
        print("Por favor ingrese algo valido")
        
    print(decoracion)