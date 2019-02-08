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

## Estructura.

Teniendo en cuenta los requerimientos de la práctica se ha realizado la siguiente estructura:

**Se ha trabajado con menús y submenús para visualizar los departamentos y tener acceso a ellos**
    
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
    
**También se ha diseñado una estructura de directorios/carpetas donde se guardan los datos**
    
![](Practica2_Funciones_departamentos/imagenes/directorios.PNG)




## Código.

```javascript
// code away!

let generateProject = project => {
  let code = [];
  for (let js = 0; js < project.length; js++) {
    code.push(js);
  }
};
```