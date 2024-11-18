from Producto import Producto
from Clientes import Clientes
from Pago import Pago
from Envio import Envio
from datetime import datetime, timedelta
from Venta import Venta
import requests
import json

venta_productos = {}
frecuencia_clientes = {}
envio_productos = {}


def eliminar_producto(lista_producto):
    while True:
        print('-'*5, "Estas en 'Eliminar producto'", '-'*5)
        salir = input(
            "Deseas eliminar un producto? si/no: ").lower().replace(" ", "")
        producto_eliminar = None
        if (salir == 'si'):
            nombre = input(
                "Ingresa el nombre del producto a eliminar: ").lower().replace(" ", "")

            for producto in lista_producto:
                if (producto.nombre.lower().replace(" ", "") == nombre):
                    producto_eliminar = producto
                    break
            if producto_eliminar:
                lista_producto.remove(producto_eliminar)
                print(f"Producto '{producto.nombre}' eliminado correctamente.")
            else:
                print("Producto no encontrado.")

        elif (salir == 'no'):
            break
        else:
            print("Ingresar si o no")
    return lista_producto


def modificar_producto(lista_producto):
    while True:
        print('-'*5, "Estas en 'Modificar producto'", '-'*5)
        salir = input("Deseas modificar un producto? si/no: ").lower()
        if (salir == 'si'):
            nombre = input(
                "Ingrese el nombre del producto a modificar: ").lower().replace(" ", "")
            lista_nombres_nombre_buscando = [
                producto for producto in lista_producto if producto.nombre.lower().replace(" ", "") == nombre]
            if not lista_nombres_nombre_buscando:
                print("sin resultados")
            else:
                print("Que deseas modificar del producto?")
                print(
                    "1)Nombre\n2)Descripcion\n3)Precio\n4)Categoria\n5)Cantidad\n6)Carros Compatibles")
                modificacion = input("--> ")
                if (modificacion == "1"):
                    for i in lista_nombres_nombre_buscando:
                        nombre_nuevo = input(
                            "Ingresa el nombre nuevo: ").lower()
                        i.nombre = nombre_nuevo
                        print("Modificado: ", i)
                elif (modificacion == '2'):
                    for i in lista_nombres_nombre_buscando:
                        descripcion_nueva = input(
                            "Ingrese la nueva descripcion: ")
                        i.descripcion = descripcion_nueva
                        print("Modificado: ", i)
                elif (modificacion == '3'):

                    for i in lista_nombres_nombre_buscando:
                        try:
                            precio_nuevo = int(
                                input("Ingresar el nuevo precio:$"))
                            i.precio = precio_nuevo
                            print("Modificado: ", i)
                        except ValueError:
                            print("Ingresar n valor numerico")
                elif (modificacion == '4'):
                    for i in lista_nombres_nombre_buscando:
                        categoria_nueva = input(
                            "Ingresar la nueva categoria: ")
                        i.categoria = categoria_nueva
                        print("Modificado: ", i)
                elif (modificacion == '5'):
                    for i in lista_nombres_nombre_buscando:
                        try:
                            cantidad = int(
                                input("Ingresa la nueva cantidad del producto: "))
                            i.inventario = cantidad
                            print("Modificado: ", i)
                        except ValueError:
                            print("Ingresar un valor numerico")
                elif (modificacion == '6'):
                    for producto in lista_nombres_nombre_buscando:
                        carros_compatibles = []
                        while True:
                            vehiculo = input(
                                "Ingrese un modelo de carro compatible (o 'listo' para terminar): ")
                            if vehiculo.lower() == 'listo':
                                break
                            carros_compatibles.append(vehiculo)
                        producto.carros_compa = carros_compatibles
                        print("Modificado: ", producto)

        elif (salir == 'no'):  # para salir del bucle
            break
        else:
            print("Dato invalido")

    return lista_producto


# funcion encargada de agregar productos a lista de productos
def agregar_producto(lista_producto):

    while True:

        print("Estas en 'Agregar producto'")
        salir = input("Desea regresar? Si/No: ").lower()
        if (salir == 'no'):
            nombre = input("Ingresa el nombre del producto: ")
            descripcion = input("Ingresa una descripcion del producto: ")
            precio = (input("Ingresa el precio en numeros del producto: $"))
            precio = validacion_int(precio)
            categoria = input("Categoria ej: aceite,filtro,empacadura etc: ")
            inventario = (input("Ingresa las cantidades: "))
            inventario = validacion_int(inventario)

            modelo = ""
            carros_compa = []
            while True:
                respuesta = input(
                    "Deseas agregar algun modelo al cual aplica el repuesto? si/no: ").lower()
                if (respuesta == 'si'):
                    modelo = input("Ingresa los modelos a los cuales aplica: ")
                    carros_compa.append(modelo)
                elif (respuesta == "no"):
                    break
                else:
                    print("Por favor, ingresa 'si' o 'no': ")

                if (modelo == ''):
                    modelo = "N/A"

            maxId = 0
            for producto in lista_producto:

                if (producto.ids) > maxId:
                    maxId = producto.ids
            nuevoId = maxId+1

            nuevoProducto = Producto(
                nuevoId, nombre, descripcion, precio, categoria, inventario, carros_compa)
            lista_producto.append(nuevoProducto)
            print(f"Producto agregado: {nuevoProducto}")
        elif (salir == 'si'):
            break
        else:
            print("Ingresa 'si' o 'no'")

    return lista_producto


def modificar_cliente(lista_clientes):
    while True:
        print("Estas en 'Gestion de Clientes'")
        salir = input("Desea regresar? Si/No: ").lower()
        if (salir == 'no'):
            print("Lista de clientes")
            for i, cliente in enumerate(lista_clientes):
                print(f"{i+1}){cliente.nombre} ID:{cliente.cedula}")

            try:
                eleccion = int(
                    input("Seleccione el cliente correspondiente al numero: "))
                cliente_modificar = lista_clientes[eleccion-1]
            except ValueError:
                print("Seleccion invalida")
                return
            print(f"\nCliente seleccionado: {cliente_modificar}")
            print("¿Qué información deseas modificar?")
            print("1. Nombre")
            print("2. Correo electrónico")
            print("3. Dirección")
            print("4. Teléfono")
            if cliente_modificar.tipo == 'J':  # Si es un cliente jurídico
                print("5. Nombre de contacto")
                print("6. Teléfono de contacto")
                print("7. Correo de contacto")

            modificacion = input("Elige una opción: ")
            if (modificacion == '1'):
                nuevo_nombre = input("Ingrese el nuevo nombre: ")
                cliente_modificar.nombre = nuevo_nombre
            elif (modificacion == '2'):
                nuevo_email = input("Ingrese el nuevo correo electrónico: ")
                cliente_modificar.correo = nuevo_email
            elif (modificacion == '3'):
                nueva_direccion = input("Ingrese la nueva dirección: ")
                cliente_modificar.direccion_envio = nueva_direccion
            elif (modificacion == '4'):
                try:
                    nuevo_telefono = int(input("Ingrese el nuevo teléfono: "))
                except ValueError:
                    print("Dato invalido")
                cliente_modificar.telefono = nuevo_telefono
            elif (modificacion == '5') and (cliente_modificar.tipo == 'J'):
                nuevo_nombre_contacto = input(
                    "Ingrese el nuevo nombre de contacto: ")
                cliente_modificar.nombre_contacto = nuevo_nombre_contacto
            elif (modificacion == '6') and (cliente_modificar.tipo == 'J'):
                try:
                    nuevo_telefono_contacto = int(
                        input("Ingrese el nuevo teléfono de contacto: "))
                except ValueError:
                    print("Dato invalido")
                cliente_modificar.telf_contacto = nuevo_telefono_contacto

            elif (modificacion == '7') and (cliente_modificar.tipo == 'J'):
                nuevo_email_contacto = input(
                    "Ingrese el nuevo correo electrónico de contacto: ")
                cliente_modificar.correo_contacto = nuevo_email_contacto
            else:
                print("Opción inválida.")
                return

            print(f"\nCliente modificado: {cliente_modificar}")
        elif (salir == 'si'):
            break
        else:
            print("dato invalido")
    return lista_clientes


def eliminar_cliente(lista_clientes):
    while True:

        print("Estas en 'Eliminar cliente'")
        salir = input("Desea regresar? Si/No: ").lower()
        if (salir == 'no'):
            cedula = (input("Ingresa la cedula del cliente a eliminar: "))
            cedula = validacion_ci(cedula)
            cliente_eliminar = None
            for i in lista_clientes:
                if i.cedula == cedula:
                    cliente_eliminar = i
            if cliente_eliminar:
                lista_clientes.remove(cliente_eliminar)
                print(f"Cliente con la cedula {cedula} fue eliminado")
            else:
                print("Cliente no encontrado")
        elif (salir == 'si'):
            break
        else:
            print("Dato invalido")
    return lista_clientes


def validacion_fecha(fecha):
    try:
        # fecha.split("/") devuelve tres elementos
        dia, mes, anio = fecha.split("/")

        # Convertir a enteros directamente
        dia = int(dia)
        mes = int(mes)
        # Asegurar que el año tiene 4 dígitos
        if len(anio) == 2:
            anio = "20" + anio  # Asumiendo que el año es en el siglo 21
        anio = int(anio)

        # Validaciones
        if dia < 1 or dia > 31:
            return False
        if mes < 1 or mes > 12:
            return False
        if anio < 2023 or anio > datetime.now().year:
            return False

        # Verificar si la fecha es válida
        datetime(anio, mes, dia)
        return True
    except ValueError:
        return False
    except IndexError:
        return False


def validacion_int(num):
    try:
        return int(num)
    except ValueError:
        print("Error: Debe ingresar un número entero.")
    while True:
        num = input("Ingrese un número valido: ")
        try:
            return int(num)
        except ValueError:
            print("Error: Debe ingresar un número entero.")


def validacion_ci(ci):
    while True:
        # Asegúrate de que validacion_int solicite un nuevo valor si es necesario
        ci = validacion_int(ci)
        if 7 <= len(str(ci)) <= 8 and ci > 0:
            return ci
        else:
            print("Error: La cédula debe tener entre 7 y 8 dígitos y ser positiva.")
            ci = input("Ingrese nuevamente la cédula: ")


def validacion_opcion(opcion, max):
    opcion = validacion_int(opcion)

    if 1 <= opcion <= max:
        return opcion
    while True:
        opcion = input("Ingrese una opcion valida: ")
        opcion = validacion_int(opcion)
        if 1 <= opcion <= max:
            return opcion
        else:
            print(f"Error: La opción debe estar entre {1} y {max}.")

# ----------------metodos para registrar-------------------------


def registrar_pago(lista_cliente, lista_pago):
    while True:
        try:
            try:
                sali = input("Deseas salir? si/no: ").lower().replace(" ", "")
                if (sali == 'si'):
                    break
            except ValueError:
                print("Dato invalido")

            cliente_cedula = (input("Ingresa la cedula del cliente: "))
            cliente_cedula = validacion_ci(cliente_cedula)

            cliente = None
            # Verificar si el cliente existe
            for i in lista_cliente:
                if i.cedula == cliente_cedula:  # Si el cliente existe
                    cliente = i
                    break

            if cliente is None:  # Si no se encuentra el cliente
                print("El cliente no existe. ¿Deseas agregarlo? si/no: ")
                opcion = input("--> ").lower()
                if opcion == 'si':
                    cliente = registrar_cliente(lista_cliente)

                else:
                    print("No se puede continuar sin un cliente. Intente nuevamente.")
                    continue  # Vuelve a pedir la cédula si no se quiere agregar el cliente

            monto = int(input("Ingresar monto exacto del monto: "))
            print("""
                  bolivares 
                  dolares
                  """)
            tipo_pago = " "
            print("Tipo de moneda")
            tipo_moneda = input("--> ").lower().replace(" ", "")

            if tipo_moneda == "dolares":
                print("""
                        1)Zelle
                        2)Paypal
                        3)Efectivo
                                """)
                tipo_pago = (input("--> "))
                tipo_pago = validacion_opcion(tipo_pago, 3)
                match tipo_pago:
                    case 1:
                        tipo_pago = 'zelle'
                    case 2:
                        tipo_pago = 'paypall'
                    case 3:
                        tipo_pago = 'efectivo'
                    case 4:
                        tipo_pago = 'Efectivo'
            elif (tipo_moneda == "bolivares"):
                print("""
                      1)Punto de venta
                      2)Pago movil
                      3)Transferencia
                      4)Efectivo
                      """)

                tipo_pago = int(input("--> "))
                tipo_pago = validacion_opcion(tipo_pago, 4)

                match tipo_pago:
                    case 1:
                        tipo_pago = 'Puntodeventa'
                    case 2:
                        tipo_pago = 'Pagomovil'
                    case 3:
                        tipo_pago = 'Transferencia'
                    case 4:
                        tipo_pago = 'Efectivo'

            fecha = input("Ingrese la fecha en formato dd/mm/yyyy: ")
            while not validacion_fecha(fecha):
                print("Fecha invalida")
                fecha = input("Ingrese la fecha en formato dd/mm/yyyy: ")

        except ValueError:
            print("Dato invalido")

        pago = Pago(cliente, monto, tipo_moneda, tipo_pago, fecha)
        print("Pago registrado: ", pago)
        lista_pago.append(pago)
    return lista_pago


def registrar_envios(lista_ventas, lista_envios):
    while True:
        salir = input("Deseas salir? (si/no): ").strip().lower()
        if salir == 'si':
            break

        try:
            cedula = (
                input("Ingresa la cedula del cliente para ver las ventas: "))
            cedula = validacion_ci(cedula)
        except ValueError:
            print("Cédula inválida. Por favor ingrese un número.")
            continue

       # buscar venta por la cedula

        for venta in lista_ventas:
            print(type(venta))
        ventas_cliente = [
            venta for venta in lista_ventas if venta.ci_cliente.cedula == cedula]

        if ventas_cliente:
            print(f"Ventas para el cliente con cédula {cedula}:")
            for i, venta in enumerate(ventas_cliente, start=1):
                print(f"\nVenta {i}:")
                venta.mostrar_desglose()  # Aquí se muestra el desglose de la venta
     # Selección de la venta
            try:
                seleccion = (
                    input("Selecciona el número de la venta que deseas registrar para envío: "))
                seleccion = validacion_int(seleccion)
                if seleccion < 1 or seleccion > len(ventas_cliente):
                    raise ValueError("Selección inválida.")
                # Seleccionar la venta
                venta_seleccionada = ventas_cliente[seleccion - 1]
                try:
                    for producto in venta_seleccionada.producto_comprado:
                        try:
                            envio_productos[producto] += 1
                        except:
                            envio_productos[producto] = 1
                except:
                    pass

            except ValueError as e:
                print(f"Error: {e}. Intenta de nuevo.")
                continue

            # Solicitar datos del envío
            servicio_envio = input(
                "Ingrese el servicio de envío (e.g., Zoom, Delivery por moto): ").strip().lower()
            costo_servicio = float(
                input("Ingrese el costo del servicio de envío: "))

            # Datos adicionales en caso de ser delivery por moto
            if servicio_envio == "delivery por moto":
                nombre_motorizado = input("Nombre del motorizado: ").strip()
                telf_motorizado = input("Teléfono del motorizado: ").strip()
                motorizado = {
                    "nombre": nombre_motorizado,
                    "telefono": telf_motorizado
                }
            else:
                motorizado = None

            fecha = input("Ingrese la fecha de envio: ")
            # Crear el objeto Envio y agregarlo a la lista de envíos
            envio = Envio(venta_seleccionada, servicio_envio,
                          costo_servicio, motorizado, fecha)
            lista_envios.append(envio)
            print("Envio registrado con exito!")

        else:
            print(
                f"No se encontraron ventas para el cliente con cédula {cedula}.")
    return lista_envios


def registrar_cliente(lista_compradores):
    nombre_cli = input("Ingresar nombre: ")
    try:
        idss = (input("Ingresar Cédula o RIF: "))
        ids = validacion_ci(idss)
        telf_contacto = ""
    except ValueError:
        print("Dato invalido")
    natural_juridico = input(
        "Escribir V (persona natural) J(persona juridica): ").upper().replace(" ", "")

    nombre_contacto = ""

    email_contacto = ""

    if natural_juridico == 'J':
        nombre_contacto = input("Ingresar nombre del contacto: ")
        telf_contacto = (input("Ingresar telefono del contacto: "))
        telf_contacto = validacion_int(telf_contacto)
        email_contacto = input(
            "Ingresar email del contacto sin agregar '@gmail.com': ")+'@gmail.com'

    email = input(
        "Ingresar correo electronico sin agregar '@gmail.com': ")+'@gmail.com'
    direccion = input("Ingresar direccion: ")
    telefono = (input("Ingresar telefono: "))
    telefono = validacion_int(telefono)
    clientico = Clientes(nombre_cli, ids, email, direccion, telefono,
                         natural_juridico, nombre_contacto, telf_contacto, email_contacto)
    lista_compradores.append(clientico)
    print(" ")
    print("Cliente agregado: ", clientico.nombre, clientico.cedula)
    return clientico


def actualizar_productos_txt(lista_producto, archivo="estado.txt"):
    # Guardar la lista actualizada de productos en el archivo
    with open(archivo, "w", encoding="UTF-8") as f:
        # Convertir la lista de productos a diccionarios para almacenarla en formato JSON
        json.dump([producto.__dict__ for producto in lista_producto], f)


def registrar_ventas(lista_ventas, lista_cliente, lista_producto, lista_pago):
    while True:
        print("Estas en 'Registrar ventas' ")
        salir = input("Desea regresar? Si/No: ").lower()
        if (salir == 'no'):
            cliente_cedula = (input("Ingresa la cedula del cliente: "))
            cliente_cedula = validacion_int(cliente_cedula)
            cliente = None
            # Verificar si el cliente existe
            for i in lista_cliente:
                if i.cedula == cliente_cedula:  # Si el cliente existe
                    cliente = i
                    break

            if cliente is None:  # Si no se encuentra el cliente
                print("El cliente no existe. ¿Deseas agregarlo? si/no: ")
                opcion = input("--> ").lower()
                if opcion == 'si':
                    cliente = registrar_cliente(lista_cliente)
                else:
                    print("No se puede continuar sin un cliente. Intente nuevamente.")
                    continue  # Vuelve a pedir la cédula si no se quiere agregar el cliente
            try:
                frecuencia_clientes[cliente] += 1
            except:
                frecuencia_clientes[cliente] = 1
            producto_comprado = []
            cantidades = []
            while True:
                for idx, producto in enumerate(lista_producto, start=1):
                    print(f"{idx}. ID: {producto.ids} - Nombre: {producto.nombre}")
                seleccion = (
                    input("Ingresa el numero del producto correspondiente: "))
                seleccion = validacion_int(seleccion)
                if 1 <= seleccion <= len(lista_producto):
                    # se usa seleccion - 1 para obtener el indice correcto
                    producto_seleccionado = lista_producto[seleccion - 1]
                    print(f"Has seleccionado el producto: {producto_seleccionado.nombre}")
                    cant_producto = (
                        input("Ingresa la cantidad del producto comprado: "))
                    cant_producto = validacion_int(cant_producto)

                    if cant_producto <= producto_seleccionado.inventario:  # Verifica si hay suficiente stock
                        try:
                            venta_productos[producto_seleccionado] += cant_producto
                        except:
                            venta_productos[producto_seleccionado] = cant_producto

                        producto_comprado.append(producto_seleccionado)
                        cantidades.append(cant_producto)
                        # Reducir la cantidad en el producto seleccionado
                        producto_seleccionado.inventario -= cant_producto
                    else:
                        print(f"No hay suficiente stock de {producto_seleccionado.nombre}. Solo hay {producto_seleccionado.inventario} unidades.")
                        continue  # Si no hay suficiente stock, pide la cantidad de nuevo
                else:
                    print("Selección inválida. Intente nuevamente.")

                salir = input("Deseas seguir agregando?si/no: ").lower()
                if salir == 'no':
                    break

            metodo_pago = input(
                "Ingresa el metodo de pago dolares/bolivares: ").lower().replace(" ", "")
            metodo_envio = input(
                "Ingrese el metodo del envio: ").lower().replace(" ", "")
            fecha = input(
                "Ingrese la fecha en formato dd/mm/yyyy: ").replace(" ", "")
            validacion_fecha(fecha)
            nueva_venta = Venta(cliente, metodo_pago, metodo_envio,
                                producto_comprado, cantidades, fecha)
            lista_ventas.append(nueva_venta)  # lo agrego a la lista de ventas
            print(" ")
            print("Venta Registrada con exito!")
            print(" ")
            nueva_venta.mostrar_desglose()

            # Actualizar el archivo de productos con las cantidades actualizadas
            actualizar_productos_txt(lista_producto)

            print(" ")
        elif salir == 'si':
            break
    return lista_ventas


def registrar_ventas_old(lista_ventas, lista_cliente, lista_producto, lista_pago):
    while True:
        print("Estas en 'Registrar ventas' ")
        salir = input("Desea regresar? Si/No: ").lower()
        if (salir == 'no'):
            cliente_cedula = (input("Ingresa la cedula del cliente: "))
            cliente_cedula = validacion_ci(cliente_cedula)
            cliente = None
            # Verificar si el cliente existe
            for i in lista_cliente:
                if i.cedula == cliente_cedula:  # Si el cliente existe
                    cliente = i
                    break

            if cliente is None:  # Si no se encuentra el cliente
                print("El cliente no existe. ¿Deseas agregarlo? si/no: ")
                opcion = input("--> ").lower()
                if opcion == 'si':
                    cliente = registrar_cliente(lista_cliente)
                else:
                    print("No se puede continuar sin un cliente. Intente nuevamente.")
                    continue  # Vuelve a pedir la cédula si no se quiere agregar el cliente

            producto_comprado = []
            cantidades = []
            while True:
                for idx, producto in enumerate(lista_producto, start=1):
                    print(f"{idx}. ID: {producto.ids} - Nombre: {producto.nombre}")
                seleccion = (
                    input("Ingresa el numero del producto correspondiente: "))
                seleccion = validacion_int(seleccion)
                if 1 <= seleccion <= len(lista_producto):
                    # se usa seleccion - 1 para obtener el indice correcto
                    producto_seleccionado = lista_producto[seleccion - 1]
                    print(f"Has seleccionado el producto: {producto_seleccionado.nombre}")
                    cant_producto = int(
                        input("Ingresa la cantidad del producto comprado: "))

                    producto_comprado.append(producto_seleccionado)
                    cantidades.append(cant_producto)

                else:
                    print("Selección inválida. Intente nuevamente.")

                salir = input("Deseas seguir agregando?si/no: ").lower()
                if (salir == 'no'):
                    break
            metodo_pago = input(
                "Ingresa el metodo de pago dolares/bolivares: ").lower().replace(" ", "")
            metodo_envio = input(
                "Ingrese el metodo del envio: ").lower().replace(" ", "")
            fecha = input(
                "Ingrese la fecha en formato dd/mm/yyyy: ").replace(" ", "")
            validacion_fecha(fecha)
            nueva_venta = Venta(cliente, metodo_pago, metodo_envio,
                                producto_comprado, cantidades, fecha)
            lista_ventas.append(nueva_venta)  # lo agrego a la lista de ventas
            print(" ")
            print("Venta Registrada con exito!")
            print(" ")
            nueva_venta.mostrar_desglose()
            print(" ")
        elif (salir == 'si'):
            break

# --------------metodos para buscar -------------------


def buscar_pago(lista_pago):
    while True:
        print('-'*5, "Estas en 'Buscar producto'", '-'*5)
        print("Selecciona la opcion de busqueda con el numero respectivo")
        print(f"""
            1)Cliente
            2)Fecha
            3)Moneda de pago
            4)Tipo de pago
            5)Regresar
                  """)
        opcion = (input("--> "))
        opcion = validacion_opcion(opcion, 5)
        if (opcion == 1):  # cedula
            cedula = (input("Ingresa la cedula: "))
            cedula = validacion_ci(cedula)

            pagos_cliente = [
                pago for pago in lista_pago if pago.cliente.cedula == cedula]
            for pago in pagos_cliente:
                print("Pagos: ", pago)

        elif (opcion == 2):  # fecha
            fecha_buscada = input(
                "Ingrese la fecha en formato dd/mm/yyyy: ").replace(" ", "")
            if validacion_fecha(fecha_buscada):
                print("Fecha valida: "+fecha_buscada)
                pago_fecha = [
                    fecha for fecha in lista_pago if fecha.fecha == fecha_buscada]
                for f in pago_fecha:
                    print("Pagos: ", f)
            else:
                print("Fecha inválida. Por favor ingrese en formato dd/mm/yyyy.")

        elif (opcion == 3):  # moneda
            moneda_buscada = input(
                "Ingresa la moneda buscada: ").replace(" ", "").lower()
            pago_moneda = [
                monedita for monedita in lista_pago if monedita.moneda == moneda_buscada]
            if pago_moneda:
                for m in pago_moneda:
                    print("Pago: ", m)
            else:
                print("No se encontraron pagos con la moneda especificada.")

        elif (opcion == 4):  # tipo de pago
            tipo_depago = input(
                "Ingresa el tipo de pago: ").lower().replace(" ", "")
            tipo_paguinio = [
                paid for paid in lista_pago if paid.tipo_pago == tipo_depago]
            if tipo_paguinio:
                for i in tipo_paguinio:
                    print("Pago", i)
            else:
                print("No se encontraron pagos con el metodo de pago especificado.")

        elif (opcion == 5):
            break


def buscar_envios_por_nombre(lista_envios):
    while True:
        salir = input("¿Desea salir? 'si/no': ")
        if salir.lower() == 'no':
            nombre = input("Ingresa el nombre del cliente que deseas buscar: ")
            encontrado = False
            for envio in lista_envios:
                if envio.venta.ci_cliente.nombre.lower() == nombre.lower():
                    print(envio)
                    encontrado = True
            if not encontrado:
                print("No se encontraron envíos para el nombre ingresado.")
        elif salir.lower() == 'si':
            break
        else:
            print("Dato inválido")


def buscar_envios_por_fecha(lista_envios):
    while True:
        salir = input("¿Desea salir? 'si/no': ")
        if salir.lower() == 'no':
            fecha = input("Ingresa la fecha del envio que desea buscar: ")
            fecha_busqueda = datetime.strptime(
                fecha_busqueda, '%d/%m/%Y').date()
            encontrado = False
            for envio in lista_envios:
                # Accede directamente al nombre del cliente en la venta
                # Asegúrate de que `nombre_cliente` es el atributo en `Venta`
                if datetime.strptime(envio.fecha, '%d/%m/%Y').date() == fecha_busqueda:
                    print(envio)
                    encontrado = True
            if not encontrado:
                print("No se encontraron envíos para la fecha ingresada.")
        elif salir.lower() == 'si':
            break
        else:
            print("Dato inválido")


def buscar_producto(lista_producto):
    while True:
        print('-'*5, "Estas en 'Buscar producto'", '-'*5)
        print("Selecciona la opcion de busqueda con el numero respectivo")
        print(f"""
            1)Categoria
            2)Precio
            3)Nombre
            4)Disponibilidad
            5)Regresar
            """)
        opcion = (input("--> "))
        opcion = validacion_opcion(opcion, 5)
        if (opcion == 1):
            # se crea una lista apartir de las categorias de los productos sin repetirlas
            categorias_unicas = {
                producto.categoria for producto in lista_producto}
            print(f"Categorias disponibles:{categorias_unicas}")

            categorias = list(categorias_unicas)
            # se enumeran lascategorias para que el usuario las elija con respecto al numerpo
            for indice, categoria in enumerate(categorias, 1):
                print(f"{indice}) {categoria}")

                # se resta 1 a la entrada del usuario porque en la lista los indices comienzan desde el 0
            opcionUser = (
                input("Seleccione el numero correspondiente a la categoria: "))
            opcionUser = validacion_int(opcionUser) - 1
            categoria_seleccionada = categorias[opcionUser]
            # se crea una lista de los productos con sus detalles mientras sean iguales a la categoria elegida
            producto_elegido = [
                producto for producto in lista_producto if producto.categoria == categoria_seleccionada]
            print(f"Lista de productos de la categoria {categoria_seleccionada}")
            for i in producto_elegido:
                print(i, "\n")

        elif (opcion == 2):  # por precio
            minimo = (input("Ingresa el precio minimo que deseas buscar: "))
            minimo = validacion_int(minimo)
            maximo = (input("Ingresa el precio maximo que deseas buscar: "))
            maximo = validacion_int(maximo)
            lista_precio = [
                producto for producto in lista_producto if minimo < producto.precio < maximo]
            print("Estos son los productos que estan en el rango seleccionado: ")
            for i in lista_precio:
                print(i, "\n")

        elif (opcion == 3):  # por nombre
            nombre = input(
                "Ingrese el nombre del producto: ").lower().replace(" ", "")
            lista_nombres_nombre_buscando = [
                producto for producto in lista_producto if producto.nombre.lower().replace(" ", "") == nombre]
            if not lista_nombres_nombre_buscando:
                print("sin resultados")
            else:
                print("Lista de productos con el nombre ", nombre)
                for i in lista_nombres_nombre_buscando:
                    print(i, "\n")

        elif (opcion == 4):  # por disponibilidad
            cantidad_min = (
                input("Ingresar la cantidad minima de los productos: "))
            cantidad_min = validacion_int(cantidad_min)
            cantidad_max = int(
                input("Ingresar la cantidad maxima de los productos: "))
            cantidad_max = validacion_int(cantidad_max)
            lista_productos_disponibilidad = [
                producto for producto in lista_producto if cantidad_min < producto.inventario < cantidad_max]
            for i in lista_productos_disponibilidad:

                print(i, "\n")
        elif (opcion == 5):
            break
        else:
            print("selecciona un numero correspondiente a las opciones")


def buscar_cliente(lista_cliente):
    while True:
        print("Estas en 'Buscar cliente'")
        salir = input("Desea regresar? Si/No: ").lower()

        if salir == 'si':
            break  # Salir del bucle principal

        elif salir == 'no':
            print("Selecciona el número correspondiente:")
            print("""
                  1) Buscar por Cédula/RIF
                  2) Buscar por Email""")

            opcion = input("--> ")
            opcion = validacion_opcion(opcion, 2)
            cliente_buscado = None

            if opcion == 1:  # Búsqueda por cédula
                cedula_buscar = input(
                    "Ingresa la cédula del cliente a buscar: ")
                cedula_buscar = validacion_ci(cedula_buscar)
                for i in lista_cliente:
                    if i.cedula == cedula_buscar:
                        cliente_buscado = i
                        print("Cliente encontrado:", cliente_buscado)
                        break  # Terminar la búsqueda si se encuentra
                if not cliente_buscado:
                    print("Cliente no encontrado. Intenta nuevamente.")

            elif opcion == 2:  # Búsqueda por email
                correo_buscar = input(
                    "Ingrese el correo a buscar sin agregar '@gmail.com': ") + '@gmail.com'
                for i in lista_cliente:
                    if i.correo == correo_buscar:
                        cliente_buscado = i
                        print("Cliente encontrado:", cliente_buscado)
                        break  # Terminar la búsqueda si se encuentra
                if not cliente_buscado:
                    print("Cliente no encontrado. Intenta nuevamente.")

        else:
            print("Dato inválido. Por favor, responde con 'Si' o 'No'.")


def buscar_ventas(lista_ventas):
    while True:
        print("Estas en 'Buscar Venta'")
        salir = input("Desea regresar? Si/No: ").lower()

        if salir == 'no':
            print("Selecciona el número correspondiente: ")
            print("""
                  1) Cliente
                  2) Fecha
                  """)
            opcion = (input("--> "))
            opcion = validacion_opcion(opcion, 2)

            if opcion == 1:
                cedula = (
                    input("Ingresa la cedula del cliente para ver las ventas: "))
                cedula = validacion_ci(cedula)

                ventas_cliente = [
                    venta for venta in lista_ventas if venta.ci_cliente.cedula == cedula]

                if ventas_cliente:
                    print(f"Ventas para el cliente con cédula {cedula}:")
                    for i, venta in enumerate(ventas_cliente, start=1):
                        print(f"\nVenta {i}:")
                        venta.mostrar_desglose()  # Aquí se muestra el desglose de la venta
                else:
                    print(
                        f"No se encontraron ventas para el cliente con cédula {cedula}.")

            elif opcion == 2:
                fecha_buscada = input(
                    "Ingrese la fecha en formato dd/mm/yyyy: ").replace(" ", "")
                if validacion_fecha(fecha_buscada):
                    print("Fecha valida: "+fecha_buscada)
                    pago_fecha = [
                        fecha for fecha in lista_ventas if fecha.fecha == fecha_buscada]
                    for f in pago_fecha:
                        f.mostrar_desglose()
                else:
                    print("Fecha invalida. Debe ser formato dd/mm/yyyy")

        elif salir == 'si':
            break
        else:
            print("Opción inválida. Por favor, ingresa 'si' o 'no'.")

# --------------------------------------------------------

# ----------------------gestiones-------------------------


# funcion encargada de cumplir con el cuaarto punto
def gestion_envios(lista_ventas, lista_clientes, lista_pago, lista_envios):
    while True:
        print("Estas en 'Gestion de Envios'")
        print("Seleccionar una opcion correspondiente a su numero")
        print("""
            1)Registrar los envíos
            2)Buscar envíos
            3)Regresar
            """)
        opcion = (input("--> "))
        opcion = validacion_opcion(opcion, 3)
        if (opcion == 1):
            lista_envios = registrar_envios(lista_ventas, lista_envios)
        elif (opcion == 2):
            buscar_envios_por_nombre(lista_envios)
        elif opcion == 3:
            break
        else:
            print("Dato invalido")


# funcion encargada de cumplir con el cuaarto punto
def gestion_pagos(lista_ventas, lista_pago):
    while True:
        print("Estas en 'Gestion de Pagos'")

        print("Seleccionar una opcion correspondiente a su numero")
        print("""
            1)Registrar pago
            2)Buscar pago
            3)Salir
            """)
        opcions = input("--> ").replace(" ", "")
        opcion = validacion_opcion(opcions, 3)
        if (opcion == 1):
            lista_pago = registrar_pago(lista_ventas, lista_pago)
        elif (opcion == 2):
            buscar_pago(lista_pago)
        elif opcion == 3:
            break
        else:
            print("Dato invalido")


# funcion encarga de cumplir con el primer puntogestionar productos
def gestion_productos(lista_producto):

    while True:
        print("Estas en 'Gestion de producto'")
        print("Seleccione la opcion correspondiente al numero")
        print("""
            1)Agregar Producto
            2)Buscar producto
            3)Modificar producto
            4)Eliminar producto
            5)Regresar
              """)
        opcion = (input("--> "))
        opcion = validacion_opcion(opcion, 5)
        if (opcion == 1):
            lista_producto = agregar_producto(lista_producto)
        elif (opcion == 2):
            buscar_producto(lista_producto)
        elif (opcion == 3):
            lista_producto = modificar_producto(lista_producto)
        elif (opcion == 4):
            lista_producto = eliminar_producto(lista_producto)
        elif (opcion == 5):
            break


# funcion encargada de cumplir con el tercer punto del proyecto
def gestion_clientes(lista_clientes):
    while True:
        print("Estas en 'Gestion de Clientes'")
        salir = input("Desea regresar? Si/No: ").lower()
        if (salir == 'no'):
            print("Estas en 'Agregar cliente'")
            print("Seleccione la opcion correspondiente al numero")
            print("""
                  1)Registrar cliente
                  2)Modificar Informacion de un cliente
                  3)Eliminar clientes
                  4)Buscar Clientes
                  5)Regresar
                  """)
            opcions = (input("--> "))
            opcion = validacion_opcion(opcions, 5)
            if (opcion == 1):
                lista_clientes = registrar_cliente(lista_clientes)
            elif (opcion == 2):
                lista_clientes = modificar_cliente(lista_clientes)
            elif (opcion == 3):
                lista_clientes = eliminar_cliente(lista_clientes)
            elif (opcion == 4):
                buscar_cliente(lista_clientes)
            elif (opcion == 5):
                break
        elif (salir == 'si'):
            break
        else:
            print("Dato invalido")


# funcion encargada de cumplir con el segundo punto del proyecto
def gestion_ventas(lista_ventas, lista_cliente, lista_producto, lista_pago):
    while True:

        print("Estas en 'Gestion de Ventas'")
        print("Seleccionar una opcion correspondiente a su numero")
        print("""
            1)Registrar Venta
            2)Buscar ventas
            3)salir
            """)
        opcion = (input("--> "))
        opcion = validacion_opcion(opcion, 3)
        if (opcion == 1):
            lista_ventas = registrar_ventas(lista_ventas, lista_cliente,
                                            lista_producto, lista_pago)

        elif (opcion == 2):
            buscar_ventas(lista_ventas)
        elif (opcion == 3):
            break
        else:
            print("Dato invalido")


# funcion encargada de cumplir con el sexto punto del
def estadisticas(lista_ventas, lista_clientes, lista_pago, lista_envios):
    while True:

        print("Estas en 'Indicadores de Gestion'")
        print("Seleccionar una opcion correspondiente a su numero")
        print("""
            1)Informe Ventas
            2)Informe Pagos
            3)Informe Envios
            4)salir
            """)
        opcion = (input("--> "))
        opcion = validacion_opcion(opcion, 4)

        if (opcion == 1):
            print("Seleccionar una opcion correspondiente a su numero")
            print("""
                1)Ventas totales por día, semana, mes y año
                2)Productos más vendidos
                3)Clientes más frecuentes
                4)salir
                """)
            opcion = (input("--> "))
            opcion = validacion_opcion(opcion, 4)

            if opcion == 1:
                print("Seleccionar una opcion correspondiente a su numero")
                print("""
                    1)Ventas totales por día.
                    2)Ventas totales por semana.
                    3)Ventas totales por mes.
                    4)Ventas totales por año.
                    5)salir
                    """)
                opcion = int(input("--> "))

                # opcion = validacion_opcion(opcion, 5)
                if opcion == 1:
                    
                    ventas_diarias = {}
                    for venta in lista_ventas:
                        if venta.fecha not in ventas_diarias.keys():
                            fecha_busqueda = datetime.strptime(venta.fecha, '%d/%m/%Y').date()
                            ventas_diarias[fecha_busqueda] = 0
                            for venta2 in lista_ventas:
                                if datetime.strptime(venta2.fecha, '%d/%m/%Y').date() == fecha_busqueda:
                                    ventas_diarias[fecha_busqueda] += 1

                    ventas_ordenadas = sorted(ventas_diarias.items())
                    
                    print("Ventas diarias:")
                    for fecha in ventas_ordenadas:
                        print(f"{fecha[0]}: {fecha[1]} venta(s)")

                elif opcion == 2:
                    ventas_semanales = {}
                    for venta in lista_ventas:
                        if venta.fecha not in ventas_semanales.keys():
                            fecha_busqueda = datetime.strptime(
                                venta.fecha, '%d/%m/%Y').date()
                            inicio_semana = fecha_busqueda - \
                                timedelta(days=fecha_busqueda.weekday())
                            fin_semana = inicio_semana + timedelta(days=6)
                            ventas_semanales[fecha_busqueda] = 0
                            for venta2 in lista_ventas:
                                if inicio_semana <= datetime.strptime(venta2.fecha, '%d/%m/%Y').date() <= fin_semana:
                                    ventas_semanales[fecha_busqueda] += 1

                    ventas_ordenadas = sorted(ventas_semanales.items())
                    print("Ventas semanales:")
                    for fecha in ventas_ordenadas:
                        print(f"Semana del {fecha[0]}: {fecha[1]} venta(s)")

                elif opcion == 3:
                    ventas_mensuales = {}
                    for venta in lista_ventas:
                        if venta.fecha.month + '-' + venta.fecha.year not in ventas_mensuales.keys():
                            fecha_busqueda = datetime.strptime(
                                venta.fecha, '%d/%m/%Y').date()
                            ventas_mensuales[venta.fecha.month +
                                             '-' + venta.fecha.year] = 0
                            for venta2 in lista_ventas:
                                if fecha_busqueda.month == datetime.strptime(venta2.fecha, '%d/%m/%Y').date().month and fecha_busqueda.year == datetime.strptime(venta2.fecha, '%d/%m/%Y').date().year:
                                    ventas_mensuales[venta.fecha.month +
                                                     '-' + venta.fecha.year] += 1

                    ventas_ordenadas = sorted(ventas_mensuales.items())
                    print("Ventas mensuales:")
                    for fecha in ventas_ordenadas:
                        print(f"{fecha[0]}: {fecha[1]} venta(s)")
                elif opcion == 4:
                    ventas_mensuales = {}
                    for venta in lista_ventas:
                        if venta.fecha not in ventas_mensuales.keys():
                            fecha_busqueda = datetime.strptime(
                                venta.fecha, '%d/%m/%Y').date()
                            ventas_mensuales[fecha_busqueda.year] = 0
                            for venta2 in lista_ventas:
                                if fecha_busqueda.year == datetime.strptime(venta2.fecha, '%d/%m/%Y').date().year:
                                    ventas_mensuales[fecha_busqueda.year] += 1

                    ventas_ordenadas = sorted(ventas_mensuales.items())
                    print("Ventas semanales:")
                    for fecha in ventas_ordenadas:
                        print(f"{fecha[0]}: {fecha[1]} venta(s)")
                elif opcion == 5:
                    break

            elif opcion == 2:
                ventas_ordenadas = sorted(
                    venta_productos.items(), key=lambda item: item[1], reverse=True)
                indice = 1
                for producto in ventas_ordenadas:
                    print(
                        f"{indice}.- {producto.nombre}: {venta_productos[producto]} unidades vendidas.")
                    if indice == 5:
                        break
                    else:
                        indice += 1
            elif opcion == 3:
                clientes_ordenados = sorted(
                    frecuencia_clientes.items(), key=lambda item: item[1], reverse=True)
                indice = 1
                for cliente in clientes_ordenados:
                    print(
                        f"{indice}.- {cliente.nombre}: {frecuencia_clientes[cliente]} compras realizadas.")
                    if indice == 5:
                        break
                    else:
                        indice += 1
            elif opcion == 4:
                break

        elif (opcion == 2):
            print("Seleccionar una opcion correspondiente a su numero")
            print("""
                1)Pagos totales por día, semana, mes y año
                2)Clientes con pagos pendientes
                3)salir
                """)
            opcion = (input("--> "))
            opcion = validacion_opcion(opcion, 3)

            if opcion == 1:
                print("Seleccionar una opcion correspondiente a su numero")
                print("""
                    1)Pagos totales por día.
                    2)Pagos totales por semana.
                    3)Pagos totales por mes.
                    4)Pagos totales por año.
                    5)salir
                    """)
                opcion = (input("--> "))
                opcion = validacion_opcion(opcion, 5)
                if opcion == 1:
                    pagos_diarios = {}
                    for pago in lista_pago:
                        if pago.fecha not in pagos_diarios.keys():
                            fecha_busqueda = datetime.strptime(
                                pago.fecha, '%d/%m/%Y').date()
                            pagos_diarios[fecha_busqueda] = 0
                            for pago2 in lista_pago:
                                if datetime.strptime(pago2.fecha, '%d/%m/%Y').date() == fecha_busqueda:
                                    pagos_diarios[fecha_busqueda] += 1

                    pagos_ordenadas = sorted(pagos_diarios.items())
                    print("Pagos diarias:")
                    for fecha in pagos_ordenadas:
                        print(f"{fecha[0]}: {fecha[1]} pagos(s)")

                elif opcion == 2:
                    pagos_semanales = {}
                    for pago in lista_pago:
                        if pago.fecha not in pagos_semanales.keys():
                            fecha_busqueda = datetime.strptime(
                                pago.fecha, '%d/%m/%Y').date()
                            inicio_semana = fecha_busqueda - \
                                timedelta(days=fecha_busqueda.weekday())
                            fin_semana = inicio_semana + timedelta(days=6)
                            pagos_semanales[fecha_busqueda] = 0
                            for pago2 in lista_pago:
                                if inicio_semana <= datetime.strptime(pago2.fecha, '%d/%m/%Y').date() <= fin_semana:
                                    pagos_semanales[fecha_busqueda] += 1

                    pagos_ordenadas = sorted(pagos_semanales.items())
                    print("Pagos semanales:")
                    for fecha in pagos_ordenadas:
                        print(f"Semana del {fecha[0]}: {fecha[1]} pagos(s)")

                elif opcion == 3:
                    pagos_mensuales = {}
                    for pago in lista_pago:
                        if pago.fecha.month + '-' + pago.fecha.year not in pagos_mensuales.keys():
                            fecha_busqueda = datetime.strptime(
                                pago.fecha, '%d/%m/%Y').date()
                            pagos_mensuales[pago.fecha.month +
                                            '-' + pago.fecha.year] = 0
                            for pago2 in lista_pago:
                                if fecha_busqueda.month == datetime.strptime(pago2.fecha, '%d/%m/%Y').date().month and fecha_busqueda.year == datetime.strptime(pago2.fecha, '%d/%m/%Y').date().year:
                                    pagos_mensuales[pago.fecha.month +
                                                    '-' + pago.fecha.year] += 1

                    pagos_ordenadas = sorted(pagos_mensuales.items())
                    print("Pagos mensuales:")
                    for fecha in pagos_ordenadas:
                        print(f"{fecha[0]}: {fecha[1]} pagos(s)")
                elif opcion == 4:
                    pagos_mensuales = {}
                    for pago in lista_pago:
                        if pago.fecha not in pagos_mensuales.keys():
                            fecha_busqueda = datetime.strptime(
                                pago.fecha, '%d/%m/%Y').date()
                            pagos_mensuales[fecha_busqueda.year] = 0
                            for pago2 in lista_pago:
                                if fecha_busqueda.year == datetime.strptime(pago2.fecha, '%d/%m/%Y').date().year:
                                    pagos_mensuales[fecha_busqueda.year] += 1

                    pagos_ordenadas = sorted(pagos_mensuales.items())
                    print("Pagos semanales:")
                    for fecha in pagos_ordenadas:
                        print(f"{fecha[0]}: {fecha[1]} pagos(s)")
                elif opcion == 5:
                    break
            if opcion == 2:
                for cliente in lista_clientes:
                    pagos = 0
                    ventas = 0
                    for pago in lista_pago:
                        if pago.cliente == cliente:
                            pagos += 1
                    for venta in lista_ventas:
                        if venta.ci_cliente == cliente:
                            ventas += 1
                    if pagos != ventas:
                        print(f"{cliente.nombre} tiene {ventas-pagos} pagos pendientes.")

        elif (opcion == 3):
            print("Seleccionar una opcion correspondiente a su numero")
            print("""
                1)Envíos totales por día, semana, mes y año
                2)Productos más enviados
                3)Clientes con envíos pendientes
                4)salir
                """)
            opcion = (input("--> "))
            opcion = validacion_opcion(opcion, 4)
            if opcion == 1:
                print("Seleccionar una opcion correspondiente a su numero")
                print("""
                    1) Envíos totales por día.
                    2) Envíos totales por semana.
                    3) Envíos totales por mes.
                    4) Envíos totales por año.
                    5) salir
                    """)
                opcion = (input("--> "))
                opcion = validacion_opcion(opcion, 5)
                if opcion == 1:
                    envios_diarios = {}
                    for envio in lista_envios:
                        if envio.fecha not in envios_diarios.keys():
                            fecha_busqueda = datetime.strptime(
                                envio.fecha, '%d/%m/%Y').date()
                            envios_diarios[fecha_busqueda] = 0
                            for envio2 in lista_envios:
                                if datetime.strptime(envio2.fecha, '%d/%m/%Y').date() == fecha_busqueda:
                                    envios_diarios[fecha_busqueda] += 1

                    envios_ordenados = sorted(envios_diarios.items())
                    print("Envíos diarios:")
                    for fecha in envios_ordenados:
                        print(f"{fecha[0]}: {fecha[1]} envío(s)")

                elif opcion == 2:
                    envios_semanales = {}
                    for envio in lista_envios:
                        if envio.fecha not in envios_semanales.keys():
                            fecha_busqueda = datetime.strptime(
                                envio.fecha, '%d/%m/%Y').date()
                            inicio_semana = fecha_busqueda - \
                                timedelta(days=fecha_busqueda.weekday())
                            fin_semana = inicio_semana + timedelta(days=6)
                            envios_semanales[fecha_busqueda] = 0
                            for envio2 in lista_envios:
                                if inicio_semana <= datetime.strptime(envio2.fecha, '%d/%m/%Y').date() <= fin_semana:
                                    envios_semanales[fecha_busqueda] += 1

                    envios_ordenados = sorted(envios_semanales.items())
                    print("Envíos semanales:")
                    for fecha, total_envios in envios_ordenados:
                        print(f"Semana del{fecha[0]}: {fecha[1]} envío(s)")

                elif opcion == 3:
                    envios_mensuales = {}
                    for envio in lista_envios:
                        if f"{envio.fecha.month}-{envio.fecha.year}" not in envios_mensuales.keys():
                            fecha_busqueda = datetime.strptime(
                                envio.fecha, '%d/%m/%Y').date()
                            envios_mensuales[f"{envio.fecha.month}-{envio.fecha.year}"] = 0
                            for envio2 in lista_envios:
                                if (fecha_busqueda.month == datetime.strptime(envio2.fecha, '%d/%m/%Y').date().month and
                                        fecha_busqueda.year == datetime.strptime(envio2.fecha, '%d/%m/%Y').date().year):
                                    envios_mensuales[f"{envio.fecha.month}-{envio.fecha.year}"] += 1

                    envios_ordenados = sorted(envios_mensuales.items())
                    print("Envíos mensuales:")
                    for fecha in envios_ordenados:
                        print(f"{fecha[0]}: {fecha[1]} envío(s)")

                elif opcion == 4:
                    envios_anuales = {}
                    for envio in lista_envios:
                        if envio.fecha not in envios_anuales.keys():
                            fecha_busqueda = datetime.strptime(
                                envio.fecha, '%d/%m/%Y').date()
                            envios_anuales[fecha_busqueda.year] = 0
                            for envio2 in lista_envios:
                                if fecha_busqueda.year == datetime.strptime(envio2.fecha, '%d/%m/%Y').date().year:
                                    envios_anuales[fecha_busqueda.year] += 1

                    envios_ordenados = sorted(envios_anuales.items())
                    print("Envíos anuales:")
                    for fecha in envios_ordenados:
                        print(f"{fecha[0]}: {fecha[1]} envío(s)")

                elif opcion == 5:
                    break

            elif opcion == 2:
                envios_ordenados = sorted(
                    envio_productos.items(), key=lambda item: item[1], reverse=True)
                indice = 1
                for producto in envios_ordenados:
                    print(
                        f"{indice}.- {producto.nombre}: {envio_productos[producto]} envios realizados.")
                    if indice == 5:
                        break
                    else:
                        indice += 1
            elif opcion == 3:
                for cliente in lista_clientes:
                    envios = 0
                    ventas = 0
                    for envio in lista_envios:
                        if envio.cliente == cliente:
                            envios += 1
                    for venta in lista_ventas:
                        if venta.ci_cliente == cliente:
                            ventas += 1
                    if envios != ventas:
                        print(f"{cliente.nombre} tiene {ventas-envios} envios pendientes.")
        elif (opcion == 4):
            break
        else:
            print("Dato invalido")

# ------main---------


def main():  # funcion encargada de la gestion de menu del programa
    lista_producto = consumoAPI()
    lista_clientes = cargar_clientes()
    lista_ventas = cargar_ventas()
    lista_pago = cargar_pagoss()
    lista_envios = cargar_envios()

    while True:
        print("-"*10, "Bienvenido a la tienda de productos", "-"*10)
        print("Selecciona una de las opciones con el numero correspondiente:")
        print("""
                1)Gestion de productos
                2)Gestion de ventas
                3)Gestion de clientes
                4)Gestion de pagos
                5)Gestion de envios
                6)Estadisticas
                7)Salir""")
        #try:
        if True:
            respuesta = (input("--> "))
            respuetsa = validacion_opcion(respuesta, 7)

            if (respuetsa == 1):
                gestion_productos(lista_producto)
            elif (respuetsa == 2):
                gestion_ventas(lista_ventas, lista_clientes,
                               lista_producto, lista_pago)
            elif (respuetsa == 3):
                gestion_clientes(lista_clientes)
            elif (respuetsa == 4):
                gestion_pagos(lista_ventas, lista_pago)
            elif (respuetsa == 5):
                gestion_envios(lista_ventas, lista_clientes,
                               lista_pago, lista_envios)
            elif (respuetsa == 6):
                estadisticas(lista_ventas, lista_clientes,
                             lista_pago, lista_envios)

            elif (respuetsa == 7):
                guardar_producto_txt(lista_producto)
                guardar_clientes_txt(lista_clientes)
                guardar_pago_txt(lista_pago)
                guardar_venta_txt(lista_ventas)
                guardar_envio_txt(lista_envios)
                print("Adios :)")
                break

        #except ValueError:
            
            print("Ingrese un numero valido")
# ---------funciones de cargado desde el txt-------------------------


def cargar_pagoss():
    try:
        with open('pago.txt', 'r', encoding='UTF-8') as archivo:
            # Verificar si el archivo está vacío
            contenido = archivo.read().strip()
            if not contenido:
                print("El archivo de pagos está vacío. Se iniciará con una lista vacía.")
                return []  # Devuelve una lista vacía si el archivo está vacío

            # Si no está vacío, regresa el puntero al inicio para cargar el JSON
            archivo.seek(0)
            datos = json.load(archivo)
            lista_pagos = [Pago(**pago_data) for pago_data in datos]
            return lista_pagos

    except FileNotFoundError:
        print("No se encontró el archivo de pagos. Se iniciará con una lista vacía.")
        return []
    except json.JSONDecodeError:
        print("Error al leer el archivo de pagos. Se iniciará con una lista vacía.")
        return []


def cargar_pago():
    lista_pago = []
    with open('pago.txt', 'r', encoding='UTF-8') as archivo:
        datos = json.load(archivo)
        for pago_data in datos:
            # Crear el objeto Clientes
            cliente = Clientes(**pago_data['cliente'])
            pago = Pago(cliente, pago_data['monto'], pago_data['moneda'],
                        pago_data['tipo_pago'], pago_data['fecha'])
            lista_pago.append(pago)
        return lista_pago


def cargar_pago2():
    try:
        with open('pago.txt', 'r', encoding='UTF-8') as archivo:
            venta_data = json.load(archivo)
            lista_pago = [Pago(**venta_data) for venta_data in venta_data]
            return lista_pago
    except FileNotFoundError:
        print("No se encontró el archivo de clientes. Se iniciará con una lista vacía.")
        return []
    except json.JSONDecodeError:
        print("Error al leer el archivo de clientes. Se iniciará con una lista vacía.")
        return []


def cargar_ventas():
    try:
        # Intenta leer el contenido del archivo ventas.txt
        with open('ventas.txt', 'r', encoding='UTF-8') as archivo:
            ventas_guardar = json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        # Si el archivo no existe o está vacío, devuelve una lista vacía
        ventas_guardar = []

    lista_ventas = []
    # Procesar cada venta almacenada en el archivo
    for venta_data in ventas_guardar:
        # Crear cliente a partir de los datos almacenados
        cliente = Clientes(
            nombre=venta_data["cliente"]["nombre"],
            cedula=venta_data["cliente"]["cedula"],
            correo=venta_data["cliente"]["correo"],
            direccion_envio=venta_data["cliente"]["direccion_envio"],
            telefono=venta_data["cliente"]["telefono"],
            tipo=venta_data["cliente"]["tipo"],
            nombre_contacto=venta_data["cliente"].get("nombre_contacto", ""),
            telf_contacto=venta_data["cliente"].get("telf_contacto", ""),
            correo_contacto=venta_data["cliente"].get("correo_contacto", "")
        )

        # Crear los productos a partir de los datos almacenados
        productos = [
            Producto(
                ids=prod.get("ids", None),
                nombre=prod["nombre"],
                descripcion=prod.get("descripcion", ""),
                precio=prod["precio"],
                categoria=prod.get("categoria", ""),
                inventario=prod.get("inventario", 0),
                carros_compa=prod.get("carros_compa", None)
            )
            for prod in venta_data["productos"]
        ]

        # Crear la venta con los parámetros necesarios
        venta = Venta(
            ci_cliente=cliente,  # Se pasa el cliente como un solo argumento
            metodo_pago=venta_data["metodo_pago"],
            metodo_envio=venta_data["metodo_envio"],
            producto_comprado=productos,
            cantidades=venta_data["cantidades"],
            # Fecha de la venta, si está presente
            fecha=venta_data.get("fecha", None)
        )

        # Añadir la venta a la lista de ventas
        lista_ventas.append(venta)

    return lista_ventas


def cargar_clientes():
    try:
        with open('clientes.txt', 'r', encoding='UTF-8') as archivo:
            clientes_data = json.load(archivo)
            # Convertir cada diccionario en una instancia de la clase Clientes
            lista_clientes = [Clientes(**cliente_data)
                              for cliente_data in clientes_data]
            return lista_clientes
    except FileNotFoundError:
        return []  # Devuelve una lista vacía si el archivo no existe
    except json.JSONDecodeError:
        return []  # Devuelve una lista vacía si hay un error en el formato JSON
# PENDIENTE DE TERMINAR


def cargar_envios():
    try:
        with open('envios.txt', 'r', encoding='UTF-8') as archivo:
            envios_data = json.load(archivo)
            lista_envios = []

            for envio_data in envios_data:
                # Utilizar `.get()` para evitar errores si alguna clave falta
                venta = envio_data.get("venta", None)
                # Nombre del cliente como cadena
                cliente = envio_data.get("cliente", "Cliente desconocido")
                # Lista de nombres de productos
                productos = envio_data.get("producto", [])
                cantidades = envio_data.get(
                    "cantidad", [])  # Lista de cantidades
                precio_total = envio_data.get("precio_total", 0.0)
                servicio_envio = envio_data.get(
                    "servicio_envio", "No especificado")
                costo_servicio = envio_data.get("costo_servicio", 0.0)
                # Puede ser None si no es delivery
                motorizado = envio_data.get("motorizado")
                fecha = envio_data.get('fecha', None)
                # Crear el objeto Envio con los datos básicos
                envio = Envio(
                    venta=venta,  # Venta no es necesario para el almacenamiento simplificado
                    servicio_envio=servicio_envio,
                    costo_servicio=costo_servicio,
                    motorizado=motorizado,
                    fecha=fecha
                )

                # Asignar datos adicionales al objeto Envio
                envio.cliente = cliente
                envio.productos = productos
                envio.cantidades = cantidades
                envio.precio_total = precio_total
                envio.fecha = fecha

                # Añadir el envío a la lista
                lista_envios.append(envio)

            return lista_envios

    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []


def consumoAPI():  # funcion encargada de consumir la api, gestionarla a un objeto
    lista_producto = []
    url = "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/products.json"
    try:
        obtencion = requests.get(url, timeout=10)
        obtencion.raise_for_status()
        datos = obtencion.json()
        for item in datos:
            producto = Producto(
                ids=item['id'],
                nombre=item['name'],
                descripcion=item['description'],
                precio=item['price'],
                categoria=item['category'],
                inventario=item['inventory'],
                carros_compa=item['compatible_vehicles']
            )
            lista_producto.append(producto)
        return lista_producto

    except requests.exceptions.RequestException as e:
        print("Error de tipo: ", e)
        return []
# ------------funciones de guardados en txt----------------


def guardar_pago_txt(lista_pagos):  # listo
    with open('pago.txt', 'w', encoding='UTF-8') as archivo:
        pagos_guardar = []
        for pago in lista_pagos:
            pago_dict = pago.__dict__.copy()  # Copia los atributos del objeto Pago

            # Verifica si cliente es un objeto de la clase Clientes
            if isinstance(pago.cliente, Clientes):
                # Si es un objeto, lo convierte a diccionario
                pago_dict['cliente'] = pago.cliente.__dict__
            elif isinstance(pago.cliente, dict):
                # Si ya es un diccionario, lo usa directamente
                pago_dict['cliente'] = pago.cliente
            else:
                # Manejo de error en caso de un tipo inesperado
                print("Error: el cliente no es ni un objeto Clientes ni un diccionario.")
                continue  # Salta este pago si no cumple con los tipos esperados

            pagos_guardar.append(pago_dict)

        json.dump(pagos_guardar, archivo, indent=4, ensure_ascii=False)
# metodo que lee el contenido anterior y luego agrega el nuevo


def guardar_venta_txt(lista_ventas):
    try:
        # Intenta leer el contenido existente
        with open('ventas.txt', 'r', encoding='UTF-8') as archivo:
            ventas_guardar = json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        # Si el archivo no existe o está vacío, inicia una lista vacía
        ventas_guardar = []

    # Agrega las nuevas ventas a la lista existente
    for venta in lista_ventas:
        venta_dict = {
            "fecha:": venta.fecha,
            "cliente": venta.ci_cliente.__dict__,
            "metodo_pago": venta.metodo_pago,
            "metodo_envio": venta.metodo_envio,
            "productos": [
                {"nombre": producto.nombre, "precio": producto.precio}
                for producto in venta.producto_comprado
            ],
            "cantidades": venta.cantidades,
            "subtotal": venta.subtotal,
            "descuento": venta.descuento,
            "iva": venta.iva,
            "igtf": venta.igtf,
            "total": venta.total

        }
        ventas_guardar.append(venta_dict)

    # Guarda la lista actualizada en el archivo
    with open('ventas.txt', 'w', encoding='UTF-8') as archivo:
        json.dump(ventas_guardar, archivo, indent=4, ensure_ascii=False)


def guardar_venta_txt_anterior(lista_ventas):
    with open('ventas.txt', 'w', encoding='UTF-8') as archivo:
        ventas_guardar = []
        for venta in lista_ventas:
            # Creamos un diccionario de la venta
            venta_dict = {
                "cliente": venta.ci_cliente.__dict__,  # Convierte el cliente en un diccionario
                "metodo_pago": venta.metodo_pago,
                "metodo_envio": venta.metodo_envio,
                "productos": [
                    {"nombre": producto.nombre, "precio": producto.precio}
                    for producto in venta.producto_comprado
                ],
                "cantidades": venta.cantidades,
                "subtotal": venta.subtotal,
                "descuento": venta.descuento,
                "iva": venta.iva,
                "igtf": venta.igtf,
                "total": venta.total
            }
            ventas_guardar.append(venta_dict)

        json.dump(ventas_guardar, archivo, indent=4, ensure_ascii=False)


def guardar_envio_txt(lista_envios):
    with open('envios.txt', 'w', encoding='UTF-8') as archivo:
        envios_guardar = []

        for envio in lista_envios:
            envio_dict = {
                "venta": envio.venta.to_dict(),  # Usa el método to_dict de Venta
                # Accede al nombre del cliente desde venta
                "cliente": envio.venta.ci_cliente.nombre,
                # Lista de nombres de productos
                "productos": [producto.nombre for producto in envio.venta.producto_comprado],
                "cantidades": envio.venta.cantidades,  # Cantidades de productos comprados
                "precio_total": envio.venta.total,  # Total de la venta
                "servicio_envio": envio.servicio_envio,
                "costo_servicio": envio.costo_servicio,
                "motorizado": envio.motorizado,
                "fecha": envio.fecha
            }
            envios_guardar.append(envio_dict)

        json.dump(envios_guardar, archivo, indent=4, ensure_ascii=False)


def guardar_clientes_txt(lista_clientes):
    with open('clientes.txt', 'w', encoding='UTF-8')as archivo:
        clientes_guardar = [cliente.__dict__ for cliente in lista_clientes]
        json.dump(clientes_guardar, archivo, indent=4, ensure_ascii=False)


def guardar_producto_txt(lista_producto):
    with open('estado.txt', 'w', encoding='UTF-8') as archivo:
        # Convertir cada objeto Producto a diccionario y guardarlo
        productos_guardar = [producto.__dict__ for producto in lista_producto]
        json.dump(productos_guardar, archivo, indent=4, ensure_ascii=False)

# __dict__ metodo magico que devuelve un diccionario con los atributos del objeto


main()
