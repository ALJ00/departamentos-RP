import csv
import time
import random
import os
from clases import color
from os import system

# Funcion que muestra al usuario el menu principal
def mostrar_menu_principal():
    print("---------------------------------------------------")
    print("           Bienvenido al menú principal            ")
    print("---------------------------------------------------")
    print("Selecciona opción:\n"
          "a) Servicio post-venta\n"
          "b) Ventas - Tienda\n"
          "c) Administración\n"
          "d) Taller\n"
          "e) Marketing\n"
          "f) Salir del sistema")
    opcion = input("Opción: ")
    return opcion

# Funcion que se encarga de dar de alta un nuevo usuario en el sistema
def altaUsuario(usuario, password):
    # Controlo que usuario y password no vengan vacíos.
    if len(usuario) < 5 or len(password) < 5:
        print("Error, el usuario y la contraseña deben contener mínimo 5 caracteres.")
    else:
        # Variables de control
        a = 0
        b = 0

        # Cargo el fichero csv y lo recupero en una lista
        usuarios = leer_csv("usuarios.csv")

        for row in usuarios:
            # Contabilizo
            if usuario in row:
                a += 1
            elif password in row:
                b += 1

        if a > 0:
            print("Usuario existente")

        elif b > 0:
            print("Contraseña existente")
        else:
            fields = [usuario, password]
            with open("usuarios.csv", "a+", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(fields)
        print("Usuario dado de alta en el sistema correctamente")

# Funcion principal sistema_rp
def sistema_rp():
    # Mientras sea True no se saldra del bucle While
    while True:
        # Muestro el menu y cojo el operando retornado por la funcion mostrar_menu_principal() que es quien interactua
        # con el usuario
        operando = mostrar_menu_principal()

        # Compruebo las diferentes opciones y en cada opcion se llama a la funcion correspondiente
        # quien se encarga de abrir el menú del módulo.
        if operando == "a":
            # Compruebo credenciales de usuario
            if menu_verificacion_usuario_contrasenya():
                opcionMenuPostVenta()
        elif operando == "b":
            # Compruebo credenciales de usuario
            if menu_verificacion_usuario_contrasenya():
                opcionMenuVentas()
        elif operando == "c":
            # Compruebo credenciales de usuario
            u = input("Usuario: ")
            c = input("Contraseña: ")
            if u == "admin" and c == "admin":
                print("Credenciales de ADMINISTRADOR correctas")
                opcionMenuAdministracion()
            else:
                print("Credenciales de ADMINISTRADOR INCORRECTAS")

        elif operando == "d":
            # Compruebo credenciales de usuario
            if menu_verificacion_usuario_contrasenya():
                opcion_menu_taller()
        elif operando == "e":
            # Compruebo credenciales de usuario
            if menu_verificacion_usuario_contrasenya():
                opcionMenuMarketing()
        elif operando == "f":
            print("Agur, mila esker...")
            break
        # En caso de introducir un dato erroneo se retorna al inicio del bucle
        else:
            input("Error, seleccione una opción correcta, pulsa INTRO/RETURN  para continuar... ")

# Funcion que muestra el menu gestion de usuarios y devuelve una opcion
def mostrarSubmenuGestionUsuarios():
    mi_string = color.BLUE + " Submenú gestión de usuarios ".capitalize().upper() + color.END
    print(mi_string.center(50, "="))
    print("Selecciona opción:\n"
          "a) Nuevo usuario\n"
          "b) Borrar usuario\n"
          "c) Mostrar usuarios\n"
          "d) Salir del submenú")
    opcion = input("Opción: ")
    return opcion

# Funcion para mostrar opciones del menu usuario
def opcionSubmenuGestionUsuarios():
    while True:

        # Recojo el operando seleccionado
        operando = mostrarSubmenuGestionUsuarios()

        # Si es a doy de alta al usuario
        if operando == "a":
            u = input("Usuario: ")
            c = input("Password: ")
            altaUsuario(u, c)

        # Si es b, borro al usuario
        elif operando == "b":

            user = input("Usuario: ")
            password = input("Password: ")

            filaBorrar = []

            lista_usuarios = leer_csv("usuarios.csv")
            nueva_lista_usuarios = []

            # Recorro la lista
            for i in lista_usuarios:
                if user in i and password in i:
                    filaBorrar = i

            try:
                # Borro el usuario y contrasenya
                lista_usuarios.remove(filaBorrar)

                # Cargo los nuevos datos
                nueva_lista_usuarios = lista_usuarios

                escribir_csv(nueva_lista_usuarios)
                print("Usuario eliminado correctamente")

            except ValueError:
                print("Usuario, no encontrado.")



        # Si es la opcion c muestro todos los usuarios
        elif operando == "c":
            list = leer_csv("usuarios.csv")
            for i in list:
                print("Usuario: " + i[0], " Contraseña: " + i[1])

        # Si es la opcion d salgo del menu
        elif operando == "d":
            break

        # En caso de introducir un dato erroneo se retorna al inicio del bucle
        else:
            input("Error, seleccione una opción correcta, pulsa INTRO/RETURN  para continuar... ")

# Funcion que muestra el menu de compras
def mostrar_menu_postVenta():
    mi_string = color.RED + " Menú Servicio Post-Venta ".capitalize().upper() + color.END
    print(mi_string.center(50, "="))
    print("Selecciona opción:\n"
          "a) Mostrar listado de devoluciones\n"
          "b) Mostrar información de devolución\n"
          "c) Borrar devolución\n"
          "d) Generar orden de devolución proveedor\n"
          "e) Salir del menú")
    opcion = input("Opción: ")
    return opcion

# Funcion que muestra el menu de ventas
def mostrar_menu_ventas():
    mi_string = color.RED + " Menú ventas ".capitalize().upper() + color.END
    print(mi_string.center(50, "="))
    print("Selecciona opción:\n"
          "a) Nuevo venta\n"
          "b) Generar orden de reparación\n"
          "c) Mostrar ventas\n"
          "d) Generar devolución\n"
          "e) Salir del menú")
    opcion = input("Opción: ")
    return opcion

# Funcion que muestra el menu de RRHH
def mostrar_menu_Administracion():
    mi_string = color.RED + " Menú administración ".capitalize().upper() + color.END
    print(mi_string.center(50, "="))
    print("Selecciona opción:\n"
          "a) Contabilizar facturas\n"
          "b) Crear oferta de trabajo\n"
          "c) Gestión de usuarios\n"
          "d) Mostrar facturas activas\n"
          "e) Salir del menú")
    opcion = input("Opción: ")
    return opcion

# Funcion que muestra el menu de taller y devuelve la opcion seleccionada del menu
def mostar_menu_taller():
    mi_string = color.RED + " Menú taller ".capitalize().upper() + color.END
    print(mi_string.center(50, "="))
    print("Selecciona opción:\n"
          "a) Nueva orden de reparación\n"
          "b) Borrar reparación\n"
          "c) Listado de reparaciones\n"
          "d) Generar factura\n"
          "e) Salir del menú")
    opcion = input("Opción: ")
    return opcion

# Funcion que muestra el menu de marketing
def mostrar_menu_marketing():
    mi_string = color.RED + " Menú marketing ".capitalize().upper() + color.END
    print(mi_string.center(50, "="))
    print("Selecciona opción:\n"
          "a) Generar oferta\n"
          "b) Borrar oferta\n"
          "c) Mostrar contactos\n"
          "d) Crear contacto\n"
          "e) Salir del menú")
    opcion = input("Opción: ")
    return opcion

# Funcion que gestiona las opciones del menu taller
def opcion_menu_taller():
    while True:
        operando = mostar_menu_taller()
        # Compruebo las diferentes opciones y en cada una de ellas se realiza la función correspondiente
        if operando == "a":
            generar_orden_de_reparacion()
        elif operando == "b":
            numero = input("Introduzca orden de reparación a buscar: ")
            borrar_reparacion(numero)
        elif operando == "c":
            listado_reparaciones()
        elif operando == "d":
            numero = input("Introduzca orden de reparación a facturar: ")
            generarFacturaTaller(numero)

        elif operando == "e":
            break
        # En caso de introducir un dato erroneo se retorna al inicio del bucle
        else:
            input("Error, seleccione una opción correcta, pulsa INTRO/RETURN  para continuar... ")

# Funcion para comprobar si usuarioe y password son correctos
def verificacion_usuario_contrasenya(usuario, password):
    # Variables de control
    verificacion = False
    user = 0
    contra = 0
    # Cargo el fichero csv y lo recupero en una lista
    with open('usuarios.csv') as File:
        reader = csv.reader(File, delimiter=',', quotechar=',',
                            quoting=csv.QUOTE_MINIMAL)
        for row in reader:

            # Contabilizo
            if usuario in row and password in row:
                user += 1
                contra += 1
    if user > 0 and contra > 0:
        print("Usuario y contraseña correctos")
        verificacion = True
    else:
        print("Error, usuario o contraseña incorrectos")

    return verificacion

# Funcion que muestra el menu usuario contrasenya para que el usuario se loguee
def menu_verificacion_usuario_contrasenya():
    print("Usuario y contraseña ---->")
    user = input("Usuario: ")
    password = input("Password: ")

    # Guardo el valor que me retorna la funcion verificacion_usuario_contrasenya()
    verificacion = verificacion_usuario_contrasenya(user, password)

    return verificacion

# Funcion que crea una orden de reparacion
def generar_orden_de_reparacion():
    diccionario = []

    control = "s"
    while True:

        if control == "s":

            producto = input("Producto: ")
            observacion = input("Observaciones: ")

            if producto == "" or observacion == "":
                print("Error, debe introducir datos")
            else:

                linea = [producto, observacion]
                diccionario.append(linea)

                control = input("Nueva línea de reparación (s/n) ?")

        elif control == "n":

            print("Generando orden de reparación ------>")

            # Datos
            cliente = input("Nombre cliente: ")
            telefono = input("Teléfono: ")
            fecha = time.strftime("%d/%m/%y")
            mail = input("E-mail: ")

            if cliente == "" or telefono == "" or mail == "":
                print("Error, inserte todos los datos")
            else:
                cabecera = [fecha, cliente, telefono, mail]

                # Creo un nuevo contacto para el departamento de marketing
                contacto = [cliente, telefono, mail]
                generarContacto(contacto)

                ultNum = int(ultimoNumeroOrdenReparacion())

                mi_fichero = open("reparaciones/" + "orden" + str(ultNum + 1) + ".csv", "w", newline="")

                diccionario.append(cabecera)

                with mi_fichero:
                    writer = csv.writer(mi_fichero)
                    writer.writerows(diccionario)

                print("Creada correctamente orden de reparación nº {}".format(str(ultNum + 1)))

                break


        else:
            control = input("Error, introduzca un dato correcto: (s/n)")

# Funcion que lee archivo csv y devuelve una lista da datos
def leer_csv(archivoLeer):
    datos = []
    with open(archivoLeer, newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            datos.append(row)
    return datos

# Funcion que escribe un archivo csv
def escribir_csv(datos):
    lista = datos
    with open('usuarios.csv', 'w+', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(lista)

# Funcion para eliminar las ordenes de reparacion
def borrar_reparacion(numero):
    # Cargo el archivo
    archivo = "reparaciones/" + "orden" + numero + ".csv"

    try:
        # Elimino el archivo
        os.remove(archivo)
        print("Eliminida orden de reparación.")
    except IOError:
        print("Archivo no encontrado")

# Funcion que muestra una lista de reparaciones
def listado_reparaciones():
    rootDir = '.'
    for dirName, subdirList, fileList in os.walk(rootDir):
        if "reparaciones" in dirName:
            print("Lista de {}: ".format("repaciones"))
            for fname in fileList:
                print('\t%s' % fname)

# Función que me genera una nueva factura tras recibir una orden de reparación
def generarFacturaTaller(orden):
    try:
        # Busco la orden
        archivo = "reparaciones/" + "orden" + orden + ".csv"

        # Leo el archivo y creo una lista de datos
        datos = leer_csv(archivo)

        # Pido el importe de la factura
        importe = input("Importe factura: ")
        comprobar_numero_usuario(importe)
        cabecera = [importe]

        # Obtengo el numero de la ultima factura
        num = int(ultimoNumeroFactura())

        datos.append(cabecera)

        try:
            # Elimino el archivo
            os.remove(archivo)

            with open("facturas/" + "factura" + str(num + 1) + ".csv", 'w+', newline='') as f:
                writer = csv.writer(f)
                writer.writerows(datos)
            print("Creada correctamente factura nº {}".format(str(num + 1)))

        except IOError:

            print("Orden de reparación no encontrada")

    except IOError:
        print("Orden de reparación no encontrada")

# Funcion que genera una factura de venta
def generarFacturaVenta():
    diccionario = []
    control = "s"
    totalFactura = 0

    while True:

        if control == "s":

            producto = input("Producto: ")

            if producto == "":
                print("Error, revise los datos")
            else:
                valor = input("Importe: ")

                importe = comprobar_numero_usuario(valor)

                totalFactura += importe

                linea = [producto, importe]
                diccionario.append(linea)

                control = input("Nuevo producto (s/n) ?")

        elif control == "n":

            print("Generando factura de venta ------>")

            # Datos de cliente de la factura
            cliente = input("Nombre cliente: ")
            telefono = input("Teléfono: ")
            mail = input("E-mail: ")
            fecha = time.strftime("%d/%m/%y")

            if cliente == "" or telefono == "" or mail == "":

                print("Error, datos vacíos.")

            else:
                cabecera = [fecha, cliente, telefono, mail, str(totalFactura)]

                # Creo un nuevo contacto para el departamento de marketing
                contacto = [cliente, telefono, mail]
                generarContacto(contacto)

                # Obtengo el ultimo numero de la factura
                ultNum = int(ultimoNumeroFactura())

                mi_fichero = open("facturas/" + "factura" + str(ultNum + 1) + ".csv", "w+", newline="")

                diccionario.append(cabecera)

                with mi_fichero:
                    writer = csv.writer(mi_fichero)
                    writer.writerows(diccionario)

                print("Creada correctamente factura nº {}".format(str(ultNum + 1)))
                break


        else:
            control = input("Error, introduzca un dato correcto: (s/n)")

# Funcion para comprobar que el dato introducido por el usuario sea un numero
def comprobar_numero_usuario(numero):
    while True:
        num = None
        for conv in (int, float, complex):
            try:
                num = conv(numero)
                break
            except ValueError:
                pass
        if num is None:
            numero = input("Dato erróneo, inserte un numero:")
        else:
            return num
            break

# Funcion para distribuir las acciones del menu ventas
def opcionMenuVentas():
    while True:
        operando = mostrar_menu_ventas()
        # Compruebo las diferentes opciones y en cada una de ellas se realiza la función correspondiente
        if operando == "a":
            generarFacturaVenta()
        elif operando == "b":
            generar_orden_de_reparacion()
        elif operando == "c":
            listado_facturas()
        elif operando == "d":
            facturaAdevolver = input("Introduzca número de factura a devolver: ")
            generarDevolucion(facturaAdevolver)
        elif operando == "e":
            break
        # En caso de introducir un dato erroneo se retorna al inicio del bucle
        else:
            input("Error, seleccione una opción correcta, pulsa INTRO/RETURN  para continuar... ")

# Funcion para mostrar la lista de facturas
def listado_facturas():
    rootDir = '.'
    for dirName, subdirList, fileList in os.walk(rootDir):
        if "facturas" in dirName:
            print("Lista de {}: ".format("todas las facturas"))
            for fname in fileList:
                print('\t%s' % fname)

# Funcion para generar facturaDevolucion
def generarDevolucion(orden):
    try:
        # Busco la orden
        archivo = "facturas/" + "factura" + orden + ".csv"

        # Leo el archivo y creo una lista de datos
        datos = leer_csv(archivo)

        # Elimino el archivo
        os.remove(archivo)

        with open("devoluciones/" + "facturaDevolucion" + orden + ".csv", 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(datos)
        print("Creada correctamente facturaDevolución nº {}".format(orden))

    except IOError:

        print("Factura de venta no encontrada")

# Funcion que crea un nuevo contacto en archivo txt
def generarContacto(datos):

    try:
        f = open("marketing/directorioContactos/contactos.txt", 'a')
        f.write(str(datos)+"\n")
        f.close()

    except IOError:
        print("Archivo no encontrado")


# Funcion que genera un listado de contactos
def listado_contactos():
    contactos = []

    try:
        dirFichero = "marketing/directorioContactos/contactos.txt"
        with open(dirFichero, 'r',newline="") as reader:
            for line in reader:
                contactos.append(line)
        if len(contactos) == 0:
            print("No hay contactos registrados")
        else:
            for linea in contactos:
                print(linea, end="")


    except IOError:
        print("No existe un archivo de contactos")

    print("")


# Funcion para mostrar las opciones del menú Marketing
def opcionMenuMarketing():
    while True:
        operando = mostrar_menu_marketing()
        # Compruebo las diferentes opciones y en cada una de ellas se realiza la función correspondiente
        if operando == "a":
            generarOferta()
        elif operando == "b":
            num = input("Introduzca número de oferta a borrar: ")
            borrar_oferta(num)
        elif operando == "c":
            listado_contactos()
        elif operando == "d":
            nombre = input("Nombre: ")
            telf = input("Teléfono: ")
            mail = input("Mail: ")
            if nombre == "" or telf == "" or mail == "":
                print("Error, introduzca todos los datos")
            else:
                datos = [nombre, telf, mail]
                generarContacto(datos)
                print("Generado contacto correctamente")

        elif operando == "e":
            break
        # En caso de introducir un dato erroneo se retorna al inicio del bucle
        else:
            input("Error, seleccione una opción correcta, pulsa INTRO/RETURN  para continuar... ")

# Funcion para generar una oferta
def generarOferta():
    fecha = time.strftime("%d/%m/%y")
    producto = input("Producto en oferta: ")
    descripcion = input("Descripción de oferta: ")
    descuento = input("Descuento:")

    comprobar_numero_usuario(descuento)

    lineaOferta = [fecha, producto, descripcion, descuento]

    if producto == "" or descripcion == "":
        print("Error, revise los datos")
    else:

        n = int(ultimo_numero_oferta())

        dirFichero = 'marketing/ofertas/oferta' + str(n + 1) + '.txt'
        fichero = open(dirFichero, 'w')
        for l in lineaOferta:
            fichero.write(l + ",")
        fichero.close()
        print("Creada la oferta nº{} correctamente".format(str(n + 1)))

# Funcion que cuenta las ofertas activas que hay en el sistema
def contarOfertas():
    try:
        lista = []
        rootDir = '.'
        for dirName, subdirList, fileList in os.walk(rootDir):
            if "ofertas" in dirName:

                for fname in fileList:
                    lista.append(fname)

        numeroOfertas = len(lista)

        return numeroOfertas

    except IOError:
        print("No existe un archivo de contactos")

# Funcion para eliminar ofertas
def borrar_oferta(numero):
    # Cargo el archivo
    archivo = "marketing/ofertas/" + "oferta" + numero + ".txt"

    try:
        # Elimino el archivo
        os.remove(archivo)
        print("Eliminida oferta correctamente.")
    except IOError:
        print("Archivo no encontrado")


# Funcion para obtener el ultimo numero del archiv(ofertas, facturas ..) para poner numero al nuevo archivo
def ultimo_numero_oferta():
    try:
        lista = []
        rootDir = '.'
        for dirName, subdirList, fileList in os.walk(rootDir):
            if "ofertas" in dirName:

                for fname in fileList:
                    lista.append(fname)

        # Cuantos archivos hay
        numeroOfertas = len(lista)

        if numeroOfertas == 0:

            return 0

        else:
            # Cojo el ultimo
            ultimo_archivo = str(lista[numeroOfertas - 1])

            # Le doy la vuelta
            ultimo_archivo_reves = list(reversed(ultimo_archivo))

            # Preparo el dato
            dato = ""

            # Busco el numero de archivo
            for i in range(len(ultimo_archivo_reves)):
                if i == 4:
                    dato = ultimo_archivo_reves[i]

            # Retorno que numero tiene la ultima oferta
            return dato




    except IOError:
        print("No existe un archivo de ofertas")


# Funcion que devuelve el nuemero de la ultima factura
def ultimoNumeroFactura():
    try:
        lista = []
        rootDir = '.'
        for dirName, subdirList, fileList in os.walk(rootDir):
            if "facturas" in dirName:

                for fname in fileList:
                    lista.append(fname)

        # Cuantos archivos hay
        numeroFactura = len(lista)

        if numeroFactura == 0:

            return 0
        else:

            # Cojo el ultimo
            ultimo_archivo = str(lista[numeroFactura - 1])

            # Le doy la vuelta
            ultimo_archivo_reves = list(reversed(ultimo_archivo))

            # Preparo el dato
            dato = ""

            # Busco el numero de archivo
            for i in range(len(ultimo_archivo_reves)):
                if i == 4:
                    dato = ultimo_archivo_reves[i]

            # Retorno que numero tiene la ultima oferta
            return dato



    except IOError:
        print("No existe un archivo de contactos")


# Funcion que devuelve el numero de la ultima orden de reparacion
def ultimoNumeroOrdenReparacion():
    try:
        lista = []
        rootDir = '.'
        for dirName, subdirList, fileList in os.walk(rootDir):
            if "reparaciones" in dirName:

                for fname in fileList:
                    lista.append(fname)

        # Cuantos archivos hay
        numeroReparacion = len(lista)

        if numeroReparacion == 0:

            return 0

        else:

            # Cojo el ultimo
            ultimo_archivo = str(lista[numeroReparacion - 1])

            # Le doy la vuelta
            ultimo_archivo_reves = list(reversed(ultimo_archivo))

            # Preparo el dato
            dato = ""

            # Busco el numero de archivo
            for i in range(len(ultimo_archivo_reves)):
                if i == 4:
                    dato = ultimo_archivo_reves[i]

            # Retorno que numero tiene la ultima oferta
            return dato


    except IOError:
        print("No existe un archivo de contactos")


# Funcion para mostrar opciones del menu postVenta
def opcionMenuPostVenta():
    while True:

        operando = mostrar_menu_postVenta()

        # Compruebo las diferentes opciones y en cada una de ellas se realiza la función correspondiente
        if operando == "a":
            mostrarDevoluciones()
        elif operando == "b":
            num = input("Introduce el número de devolución a mostrar: ")
            obtenerInfoDevolucion(num)
        elif operando == "c":
            numero = input("Introduzca número de devolución a buscar: ")
            borrarDevolucion(numero)
        elif operando == "d":
            facturaAdevolver = input("Introduzca número de factura de devolución a devolver: ")
            generarDevolucionProveedor(facturaAdevolver)
        elif operando == "e":
            break

        # En caso de introducir un dato erroneo se retorna al inicio del bucle
        else:
            input("Error, seleccione una opción correcta, pulsa INTRO/RETURN  para continuar... ")

# Funcion que muestra las devoluciones
def mostrarDevoluciones():
    rootDir = '.'
    for dirName, subdirList, fileList in os.walk(rootDir):
        if "devoluciones" in dirName:
            print("Lista de {}: ".format("devoluciones"))
            for fname in fileList:
                print('\t%s' % fname)

# Funcion para eliminar devoluciones
def borrarDevolucion(numero):
    # Cargo el archivo
    archivo = "devoluciones/" + "facturaDevolucion" + numero + ".csv"
    try:
        # Elimino el archivo
        os.remove(archivo)
        print("Eliminida devolución correctamente.")
    except IOError:
        print("Archivo no encontrado")

# Funcion que extrae lainformacion de una devolucion concreta
def obtenerInfoDevolucion(numero):
    try:
        # Cargo el archivo
        archivo = "devoluciones/" + "facturaDevolucion" + numero + ".csv"

        # Leo el archivo csv y cargo los datos en una variable
        datos = leer_csv(archivo)

        print("------- Información de facturaDevolución {}".format(numero) + " --------")

        for i in datos:
            if len(i) == 2:
                print("Producto: " + i[0], " Precio: " + i[1])
            elif len(i) == 5:
                print("Fecha: " + i[0], " Nombre: " + i[1], " Móvil: " + i[2], " Mail: " + i[3], " Total: " + i[4])


    except IOError:
        print("Archivo no encontrado")

    print("")

# Funcion para generar facturaDevolucionProveedor
def generarDevolucionProveedor(orden):
    try:
        # Busco la orden
        archivo = "devoluciones/" + "facturaDevolucion" + orden + ".csv"

        # Leo el archivo y creo una lista de datos
        datos = leer_csv(archivo)

        # Elimino el archivo
        os.remove(archivo)

        with open("reclamacionesProveedores/" + "facturaDevolucionProveedor" + orden + ".csv", 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(datos)
        print("Creada correctamente facturaDevoluciónProveedor nº {}".format(orden))

    except IOError:

        print("Factura no encontrada")

# Funcion para distribuir las acciones del menu Administracion
def opcionMenuAdministracion():
    while True:
        operando = mostrar_menu_Administracion()
        # Compruebo las diferentes opciones y en cada una de ellas se realiza la función correspondiente
        if operando == "a":
            n = input("Introduce el número de factura a contabilizar: ")
            buscarFacturaYcontabilizar(n)
        elif operando == "b":
            generarOfertaTrabajo()
        elif operando == "c":
            opcionSubmenuGestionUsuarios()
        elif operando == "d":
            listado_facturas()
        elif operando == "e":
            break
        # En caso de introducir un dato erroneo se retorna al inicio del bucle
        else:
            input("Error, seleccione una opción correcta, pulsa INTRO/RETURN  para continuar... ")

# Funcion para generar una oferta de trabajo
def generarOfertaTrabajo():
    fecha = time.strftime("%d/%m/%y")
    puesto = input("Puesto de trabajo: ")
    descripcion = input("Descripción de oferta: ")
    remuneracion = input("Remuneración: ")

    comprobar_numero_usuario(remuneracion)

    lineaOferta = [fecha, puesto, descripcion, remuneracion]

    if puesto == "" or descripcion == "":
        print("Error, revise los datos")
    else:

        n = int(ultimo_numero_oferta())

        dirFichero = 'administracion/empleo/ofertaEmpleo' +puesto+ '.txt'
        fichero = open(dirFichero, 'w')
        for l in lineaOferta:
            fichero.write(l + ",")
        fichero.close()
        print("Creada la oferta de empleo {} correctamente".format(puesto))

#Funcion que busca una factura
def buscarFacturaYcontabilizar(numero):

    try:
        # Cargo el archivo
        archivo = "facturas/" + "factura" + numero + ".csv"

        # Leo el archivo csv y cargo los datos en una variable
        datos = leer_csv(archivo)

        #Variables para el rellenar el csv
        iT = ""
        f = ""
        c = ""

        #Cargo los datos correspondientes
        for i in datos:
            if len(i) == 5:
                iT = i[4]
                f = i[0]
                c = i[1]
            elif len(i) == 4:
                f = i[0]
                c = i[1]
            elif len(i) == 1:
                iT = i[0]

        #Cargo el archivo
        with open('contabilidad/detalleAsientos.csv', 'a', newline="") as csvfichero:
            campos = ['4309 CLIENTES FACTURAS PENDIENTES DE FORMALIZAR','numeroFactura', 'fecha', 'importe']
            writer = csv.DictWriter(csvfichero, fieldnames=campos)

            #Insertos los nuevos datos
            writer.writerow({'4309 CLIENTES FACTURAS PENDIENTES DE FORMALIZAR': c,'numeroFactura':numero, 'fecha': f,
                             'importe': iT})

        # Elimino la factura
        os.remove(archivo)

        print("Factura contabilizada correctamente")
    except IOError:
        print("Factura no encontrada")



