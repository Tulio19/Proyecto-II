**Documentación externa**

El siguiente programa emula una base de datos mediante el uso de archivo en c++.

El programa debe de leer un archivo (el que el usuario elija), después de eso debe mostrar un menú con las siguientes opciones:

Agregar producto
Buscar a un producto
Modificar los datos de un producto
Por decisión propia se le agregaron 2 opciones más al menú las cuales son.
Restricciones del programa.
Salir

El programa a su vez cuenta con ciertos parámetros o restricciones para su uso, los cuales son los siguientes;

1. Para agregar producto: el código de producto no debe repetirse

2. Para buscar producto: se debe buscar por el código, o por el nombre.

3. Para modificar datos: el código no puede modificarse, los otros atributos si

**Modo de uso**

Al correr el programa el usuario deberá de elegir alguna de las opciones que quiera realizar.
Opción #1 (Agregar un producto)
sí seleccionará la primera opción, deberá poner el nombre del archivo, "sin olvidar que este mismo debe estar en la misma carpeta que programa"
y también que al final lleve la extensión de ".txt".
posteriormente siguiente las restricciones del inicio el usuario deberá de colocar el código del producto que desea agregar, el programa
validara si el código ingresado existe o no en el documento que abrimos.
si existiera el código se le mostrara un mensaje al usuario informándole que ya existe el código.
si el código no se repetí, el programa le pedirá al usuario que ingrese los respectivos datos que quiera agregar al producto.
los datos deben de ser separados por cualquier carácter, exceptuando a la "," esto para evitar errores.

y siguiendo la siguiente estructura:

nombre 
código 
precio 
proveedor
existencia
estado donde A = Aprobado y R = reprobado
descuento 

**opción #2 (Buscar a un producto)**

Cuando el usuario elija la opción 2, es decir buscar un producto
el programa le pedirá al usuario que ingrese el documento en donde se buscará el producto, posteriormente siguiente las restricciones del mismo programa
se le pedirá al usuario que ingrese el código del producto, si el código coincide con alguno de los productos el programa le mostrará al usuario la
descripción de este mismo.
caso contrario si el código no existe se le mostrará un mensaje al usuario avisándole que dicho código no existe dentro del archivo.

**Opción #3 (Modificar los datos de un producto)**

Si el usuario ingresa el número 3 el proceso que seguirá el programa será el siguiente; se le pedirá que ingrese el nombre del archivo donde se encuentra
el mismo, para luego pedirle que ingrese el código del producto que este quiera modificar, siguiendo las restricciones ya mencionadas el código de todos 
los productos no pueden ser modificado en este programa, si desea realizar dicho proceso se le recomienda hacerlo desde el archivo fuente.

si el código existe dentro del archivo, se le mostrará la descripción que contenga dicho código, para que el usuario edite dicha información a su gusto.

si el código no existe se le mostrará al usuario un mensaje donde se le indique que no hay registros dentro del mismo.

**Opción #4 (Restricciones del programa)**

Simplemente se le mostrará al usuario las restricciones ya mencionadas al inicio de este documento, para facilitar al usuario común leer este tipo de 
documentos.

**Opción #5 (Salir)**

Simplemente el programa se cerrará y se le mostrará un mensaje al usuario avisándole que dicho proceso está sucediendo.


Espero este pequeño manual le sirva para saber sobre el funcionamiento del programa encargado, espero dicho programa sea de tu agrado.