from datetime import datetime
import json

decoracion = "=" * 50

def generarFactura():
    
    print(decoracion)
    
    #Ya tenemos los datos de la mesa
    
    codigo_mesa = input("Ingrese el codigo de la mesa a atender: ")
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
            generarfactura(datos_mesa, datos_cliente, fecha_formateada, productos_a_facturar)
            
        if continuar != 1 and continuar != 2:
            #debemos combatir este error no dejar que haga error si el usuairo no elije ninguna de las 2
            print("Opción invalida")
        
    
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
        
def generarfactura(mesa, cliente, fecha, productos):
    
    print(decoracion)
    print("FACTURA")
    print(f"Cliente : {cliente["Nombre"]}")
    print(f"Mesa: {mesa["Codigo"]} -> {mesa["Nombre"]} de {mesa["Puestos"]} puestos")
    print(f"Fecha : {fecha}")
    
    total_a_pagar = 0
    
    print(f"Productos solicitados")
    print(decoracion)
    for codigo, info_producto in productos.items():
        
        subtotal = ((int(info_producto["Valor Unitario"]) + int(info_producto["Iva"])) * info_producto["Cantidad"])
        
        print(f"{info_producto["Nombre"]} : {info_producto["Cantidad"]} unidades | Total = {subtotal}")
        
        total_a_pagar += subtotal
        
    print(decoracion)
    
    
   
    print(f"Total a pagar : {total_a_pagar}")
    
    print(decoracion)
    
    print("¿Desea guardar la factura?")
    print("1. Si")
    print("2. No")
    guardar_factura = int(input("Ingrese una opción: "))
    
    if guardar_factura == 1:
        
        nombre_archivo = f"Factura para {cliente["Nombre"]}.txt"
        #Guardarlo como archivo txt
        with open(nombre_archivo, "w") as factura:
            
            factura.write(decoracion + "\n")
            factura.write("FACTURA DE VENTA \n")
            factura.write(decoracion + "\n")
            factura.write(f"Fecha : {fecha}\n")
            factura.write(f"Cliente : {cliente['Nombre']} Nº {cliente['Identificaion']}\n")
            factura.write(f"Numero de contacto : {cliente['Telefono']}")
            factura.write(f"Email : {cliente['Email']}")
            factura.write(f"Mesa : {mesa['Nombre']} Nº {mesa['Codigo']}\n")
            factura.write(decoracion + "\n")
            factura.write("PRODUCTOS\n")
            
            total_a_paga_txt = 0
            
            for codigo, info_producto in productos.items():
        
                subtotal = ((int(info_producto["Valor Unitario"]) + int(info_producto["Iva"])) * info_producto["Cantidad"])
                
                factura.write(f"{info_producto["Nombre"]} : {info_producto["Cantidad"]} unidades \n valor unitario : {info_producto["Valor Unitario"]}\n Iva : {info_producto["Iva"]} \n Total = {subtotal}\n")
                
                total_a_paga_txt += 0
                
            factura.write(f"Total a pagar = {total_a_paga_txt}")
            factura.write(decoracion + "\n")
        
    if guardar_factura == 2:
        #Imprimir subtotal de nuevo
        print("Ok haz elegido no guardar la factura")
        print(f"El total a pagar es: {total_a_pagar}")
    
    
    