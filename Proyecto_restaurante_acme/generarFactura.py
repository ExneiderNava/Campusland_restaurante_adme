from datetime import datetime

def generarFactura():
    print("======================")
    codigo_mesa = int(input("Ingrese el codigo de la mesa a atender: "))
    id_cliente = int(input("Ingrese el numero de documento del cliente: "))
    fecha_actual = datetime.datetime.now()
    
    productos_solicitados = {}
    
    
    print("Ingrese el codigo del producto que desea")
    print("Lista de productos")
    # al parecer se deben recorrer dos veces con i y j
    for clave, valor in productos.items():
        print(f"Clave: {clave} Valor: {valor}")
        
    
    
    print("======================")