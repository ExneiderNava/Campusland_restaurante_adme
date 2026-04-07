#importacion para que la fecha funcione
import datetime



#zona de funciones

def menu():
    try:
        
        opcion = 0
        
        while opcion != 6:
        
            print("=============================")
            print("Bienvenido al restaurante ACME")
            print("            MENU              ")
            print("1. Crear Productos")
            print("2. Crear Mesas")
            print("3. Crear Clientes")
            print("4. Generar Factura")
            print("5. Generar Reporte de Ventas")
            print("6. Salir")
            opcion = int(input("Ingrese una opcion : "))
            print("==============================")
            
            match opcion:
                case 1:
                    crearProductos()
                case 2:
                    crearMesas()
                case 3:
                    crearClientes()
                case 4:
                    generarFactura()
                case 5:
                    generarReporte()
                case 6:
                    print("Saliendo......")
                case _:
                    print("Opcion invalida")
                    
            
    except Exception:
        print("A ocurrrido un error :(")
        
def crearProductos():
    print("===================")
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
    
    productos[codigo] = datos_producto 
    
    print("===================")
       
def crearMesas():
    print("==================")
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
    
    mesas[codigo] = datos_mesas
        
    print("==================")    
        
def crearClientes():
    print("====================")
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
    
    clientes[identificaion] = datos_cliente
        
    print("====================")
    
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
#Diccionarios
productos = {}
mesas = {}
clientes = {}

        
#llamar funciones
menu()
