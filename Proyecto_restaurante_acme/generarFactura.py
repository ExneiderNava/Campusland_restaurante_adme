from datetime import datetime
import json

def generarFactura():
    decoracion = "=" * 50
    print(decoracion)
    
    #Ya tenemos los datos de la mesa
    codigo_mesa = int(input("Ingrese el codigo de la mesa a atender: "))
    datos_mesa = buscar_datos_jason("Mesas.json", "Codigo", codigo_mesa)
    
    if not datos_mesa:
        print("Mesa no encontrada.")
        print("No se puede inciar facturación")
        return
    
    #Ya tenemos los datos del cliente
    id_cliente = int(input("Ingrese el numero de documento del cliente: "))
    datos_cliente = buscar_datos_jason("Clientes.json", "Identificacion", id_cliente)
    
    if not datos_cliente:
        print("Cliente no encontrado")
        print("No se puede inciar la facturacion")
        return
    
    
    #ya tenemos la fecha actual formateada
    
    fecha_actual = datetime.datetime.now()
    fecha_formateada = fecha_actual.strftime("%d/%m/%y")
    
    #validar que ya se puede iniciar la factura e inciarla
    if datos_mesa and datos_cliente:
        print(f"Generando factura para {datos_cliente["Nombre"]} con la mesa {datos_mesa["Nombre"]}")
        print("Lista de productos")
        with open("productos.json", "r") as productos:
            lista_productos = json.load(productos)
            
            for items in lista_productos:
                print(f"{items["codigo"]} : {items["Nombre"]} ${items["Valor Unitario"]}")
                
        #El usuario añade los productos por medio del codigo
        
        continuar = 1
        productos_a_facturar = {}
        
        while continuar == 1:
              
            productos_elegidos = input("Ingrese el codigo del producto que desea: ")
            producto_encontrado = buscar_datos_jason("productos.json", "codigo", productos_elegidos)
            
            if producto_encontrado:
                cantidad = int(input(f"Ingrese la cantidad que desea de {producto_encontrado["Nombre"]} : "))
                
                datos_producto = {
                    "codigo": productos_elegidos, 
                    "Nombre": producto_encontrado["Nombre"], 
                    "Valor Unitario": producto_encontrado["Valor Unitario"], 
                    "Iva": producto_encontrado["Iva"],
                    "Cantidad" : cantidad
                }
                
                productos_a_facturar[productos_elegidos] = datos_producto
            else:
                print("Producto no encontrado")
                
            print("¿Desea agregar otro producto?")
            print("1. SI")
            print("2. NO")
            continuar = int(input("Ingrese la opcion: "))
            

        if continuar == 2:
            #se genera la factura
            
        if continuar != 1 and continuar != 2:
            #debemos combatir este error no dejar que haga error si el usuairo no elije ninguna de las 2
        
    
    print(decoracion)
    
    
    
def buscar_datos_jason(nombre_archivo, clave, valor):
    try:
        with open(nombre_archivo, "r") as archivo:
            datos_archivo = json.load(archivo)
            for datos in datos_archivo:
                if datos.get(clave) == valor:
                    return datos
        
    except Exception:
        print("Ha ocurrido un error :(")
    