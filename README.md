![](Practica2_Funciones_departamentos/imagenes/BikeLogo.png)
# Manual de usuario.

Este manual de usuario está redactado para entender el funcionamiento del proyecto Practica2 Funciones
departamentos.

## Objetivo de la práctica.

El objetivo del proyecto es simular el funcionamiento interno de un sistema de gestión empresarial
(ERP) creando un proyecto con el entorno de desarrollo `Pycharm` y utilizando el lenguaje de programación 
`Python 3.7`
Como requerimiento de la práctica se deben cumplir los siguientes aspectos:
- Programar 4 departamentos.
- Creación de 4 opciones por departamento.
- Persistencia de datos usando csv y txt.
- Trabajar Strings, Ficheros, Excepciones, Listas y Diccionarios.
- Funcianiemto correcto del programa.
- Crear funciones.

## Estructura.

Teniendo en cuenta los requerimientos de la práctica se ha realizado la siguiente estructura:

### Menús y submenús:
    
    ---------------------------------------------------
           Bienvenido al menú principal            
    ---------------------------------------------------
    Selecciona opción:
    a) Servicio post-venta
    b) Ventas - Tienda
    c) Administración
    d) Taller
    e) Marketing
    f) Salir del sistema
    Opción: 

    
    ========== MENÚ ADMINISTRACIÓN ==========
    Selecciona opción:
    a) Contabilizar facturas
    b) Crear oferta de trabajo
    c) Gestión de usuarios
    d) Mostrar facturas activas
    e) Salir del menú
    Opción: 
    
    
    ====== SUBMENÚ GESTIÓN DE USUARIOS ======
    Selecciona opción:
    a) Nuevo usuario
    b) Borrar usuario
    c) Mostrar usuarios
    d) Salir del submenú
    Opción: 
    
### Directorio de carpetas:
    
![](Practica2_Funciones_departamentos/imagenes/directorios.PNG)

### Interacctuación entre departamentos:
````python
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

        #Datos de cliente de la factura
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


````

Con esta función se puede ver la simulación de una ERP internamente, es decir,
la intercomunicación entre los departamentos. A la vez que se genera una factura se 
está dando de alta un nuevo contacto en el sistema. El contacto se guardaría en el archivo `contactos.txt`
y la venta se guardaría en `facturas`  y a su vez generado el archivo `facturaNº.csv`.
No obstante a través del video tutorial que se adjunta en el proyecto se podrá ver al detalle
el funcionamiento del proceso.




## Video

![Video Tutorial](https://www.youtube.com/watch?v=_nvZ9k6YpTE&feature=youtu.be)