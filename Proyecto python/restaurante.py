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
        
productos = {}

def crearProductos():
    print("\n" + "="*25)
    print("MODULO DE INGRESAR PRODUCTO")
    print("="*25)
    
 
    while True:
        try:
            codigo = int(input("Ingrese el código del producto: "))
            break
        except ValueError:
            print("Error: El código debe ser un número entero.")

    
    while True:
        nombre = input("Ingrese el nombre del producto: ")
        if nombre.replace(" ", "").isalpha():
            break
        else:
            print("Error: El nombre solo debe contener letras.")

   
    while True:
        try:
            valor_unitario = int(input("Ingrese el valor unitario: "))
            if valor_unitario > 0:
                break
            else:
                print("Error: El precio debe ser mayor a 0.")
        except ValueError:
            print("Error: Ingrese un número válido para el precio.")

    
    while True:
        try:
            iva = int(input("Ingrese el porcentaje de IVA (ej: 19): "))
            if iva >= 0:
                break
            else:
                print("Error: El IVA no puede ser negativo.")
        except ValueError:
            print("Error: Ingrese un número válido para el IVA.")

   
    datos_producto = {
        "codigo": codigo,
        "Nombre": nombre,
        "Valor Unitario": valor_unitario,
        "Iva": iva
    }
    
    productos[codigo] = datos_producto
       
mesas = {}

def crearMesas():
    print("==================")
    print("Modulo de crear mesas")
    
    
    while True:
        try:
            codigo = int(input("Ingrese el codigo de la mesa: "))
            if codigo > 0:
                break
            else:
                print("Error: El codigo debe ser un numero positivo.")
        except ValueError:
            print("Error: Ingrese un dato valido (numero entero).")

    
    while True:
        nombre = input("Ingrese el nombre de la mesa: ")
        if nombre.replace(" ", "").isalpha():
            break
        else:
            print("Error: El nombre de la mesa solo debe contener letras.")

    
    while True:
        try:
            puestos = int(input("¿Cuantos puestos tiene esta mesa?: "))
            if puestos > 0:
                break
            else:
                print("Error: La mesa debe tener al menos 1 puesto.")
        except ValueError:
            print("Error: Ingrese un numero entero para los puestos.")

    
    datos_mesas = {
        "Codigo" : codigo,
        "Nombre" : nombre,
        "Puestos" : puestos
    }
    
   
    mesas[codigo] = datos_mesas
        
    print("------------------")
    print(f"Mesa '{nombre}' creada correctamente.")
    print("==================")
        
clientes = {}

def crearClientes():
    print("====================")
    print("Modulo de Crear Clientes")
    
    
    while True:
        try:
            identificacion = int(input("Ingrese el numero de identificacion: "))
            if identificacion > 0:
                break
            else:
                print("Error: La identificacion debe ser un numero positivo.")
        except ValueError:
            print("Error: Ingrese un numero de identificacion valido.")

    
    while True:
        nombre = input("Ingrese el nombre: ")
        if nombre.replace(" ", "").isalpha():
            break
        else:
            print("Error: El nombre solo debe contener letras.")

    
    while True:
        telefono = input("Ingrese el numero de telefono: ")
        if telefono.isdigit():
            break
        else:
            print("Error: El telefono solo debe contener numeros.")

    
    while True:
        email = input("Ingrese el Email: ")
        if "@" in email and "." in email:
            break
        else:
            print("Error: Ingrese un correo electronico valido (ejemplo@correo.com).")

    # Guardar datos
    datos_cliente = {
        "Identificacion" : identificacion,
        "Nombre" : nombre,
        "Telefono" : telefono,
        "Email" : email
    }
    
    clientes[identificacion] = datos_cliente
    
    print("--------------------")
    print(f"Cliente {nombre} registrado correctamente.")
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
