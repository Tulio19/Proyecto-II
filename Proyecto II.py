#Realizar una base de datos utilizando archivos.
#Al abrir el programa debe mostrar un menú con las siguientes opciones:Agregar producto, Buscar a un producto Modificar los datos de un producto
#Siguiendo ciertas restricciones que seran explicadas en la documentación externa.
#Aún asi en el menú principal del programa esta la opcción 4 la cual corresponde a dichas restrecciones.

#Comenzamos creando nuestra funcion princial la cual nos ayudara para abrir nuestro archivo con los productos.
def abrir_archivo(nombre_archivo):
    try:
#La letra "r" funiona para que lea el archivo por completo sin ninguna acción más.
        with open(nombre_archivo, "r") as archivo:
            contenido = archivo.read()
            return contenido
    except FileNotFoundError:
        print("El archivo no se encontró.")
    return None  #todo este proceso estara guardado en "abrir_archivo."

#Creamos nuestra segunda funcion la cual consiste en guardar los datos en nuestro archivo
def guardar_archivo(nombre_archivo, contenido):
    try:
#La letra correspondiente cambia de "r↔w" esto para poder reescribir en el archivo.
        with open(nombre_archivo, "w") as archivo:
            archivo.write(contenido)
#Cuando finalice el proceso de guardado se mostrara el siguiente mensaje.

            print("Archivo guardado con éxito.\n\n*Gustas hacer una acción mas?*\n")
    except Exception as e:
#Caso contrario si el proceso fallara se mostraria el siguiente mensaje:
        print("Ocurrió un error al guardar el archivo:", str(e))

#Ahora creamos nuestra primera opciones del menu principal.
def agregar_producto(nombre_archivo, codigo, descripcion):
    datos_actuales = abrir_archivo(nombre_archivo)
    if datos_actuales is not None:
        lineas = datos_actuales.split('\n')
#Se utiliza un ciclo for para leer entre lienas y verificar si el codigo que se ingreso es repetido o no.
        for linea in lineas:
            partes = linea.split(',')
            if len(partes) == 2 and partes[0] == codigo:
#Si el codigo ingresado por el usuario se mostrara el siguiente mensaje:
                print("El código del producto ya existe en el archivo.")
                return  
            
#Caso contrario si el codigo no es repetido se realizara el siguiente proceso 
#el cual consiste en pedir al usario los nuevos datos, y se mostrara el producto al final.
        nuevos_datos = f"{codigo},{descripcion}"
        nuevo_contenido = datos_actuales + "\n" + nuevos_datos

#En esta linea se guarda lo ingresado por el usario y se suma a lo que ya se tiene en el documento.
        guardar_archivo(nombre_archivo, nuevo_contenido)

#Se mostrara el sigueinte mensaje el cual confirma que se ha agregado el producto y se muestra como queda en el documento.
        print(f"Producto agregado - Código: {codigo}, Descripción: {descripcion}")
        
#Creamos nuestro segundo proceso el cual corresponde a la segunda opcion de nuestro menu pprincipal.
#que es buscar un producto con la restricción que tiene que buscarse mediante el codigo del mismo.
#Para esto abrimos nuestro archivo y posteriormente pedimos al usuario que ingrese el codigo del archivo que este buscando.
def buscar_producto(nombre_archivo, codigo):

#creamos una variable para abrir nuestro archivo mediante el nombre del mismo.
    contenido = abrir_archivo(nombre_archivo)
    if contenido:
        lineas = contenido.split('\n')
#Posteriormente nuestro ciclo for comenzara a leer el archivo liena por linea hasta que encuentre igualada en el codigo que el usuario ingreso.
        for linea in lineas:
            partes = linea.split(',')
            if len(partes) == 2 and partes[0] == codigo:
#Si el codigo corresponde a un producto este se mostrara el panatalla con el mensaje de producto encontrado y el codigo del mismo
#y su respectiva descripción.
                print(f"Producto encontrado - Código: {partes[0]}.\n \nDescripción: {partes[1]}")
#Retornara a liena la cual imprimira lo anterior.
                return linea  
#Si el codigo no coincide con ningun producto se mostrara el siguiente mensaje.
        print("El codigo ingresado no correspondea ningun producto, intentalo de nuevo.")
    return None

#Creamos nuestro tecer proceso correspondiente a nuestra tercera opcion de nuestro menu principal "modificar algun producto"
#contara con la restricción de que el codigo no puedo ser modificado nada mas los datos del producto.
def editar_producto(nombre_archivo, codigo):
    linea = buscar_producto(nombre_archivo, codigo)
#iniciamos un if ya que nuestra funcion princial consta de depencias
    if linea:
#le pedimos al usuario que ingrese los nuevos datos segun sus necesidades.
        nueva_descripcion = input("\nEdite los datos segun sus necesidaes.\n(El codigo no debe volver a ingresarlo.): ")
        nuevos_datos = f"{codigo},{nueva_descripcion}"
#Abriremos nuestro archivo actual
        datos_actuales = abrir_archivo(nombre_archivo)
#para crear una funcion con nuestro contenido editado y sera reeemplazado el la linea correspondiente al codigo,
        contenido_editado = datos_actuales.replace(linea, nuevos_datos)
#Se guardaran los datos en nuestra funcion guardar_archivos que creamos el principio de nuestro programa.        
        guardar_archivo(nombre_archivo, contenido_editado)

#Ahora iniciamos una estructura while esto para crear nuestro menú principal.
while True:
    print("\nMenu")
#Se le mostraran las opciones disponibles al usuario, las cuales son las siguientes:
    print("1. Agregar un producto.\n2. Buscar un producto.\n3. Modificar los datos de un producto.\n4. Restricciones del programa.\n5. Salir")

#luego creamos una variable en la que le pediremos al usario que ingrese un numero correspondiente a una opcion
#en nuestro menu principal y la almacenaremos en este caso en "opcion"
    opcion = input("Ingrese el número de la opción que desea: ")

#Posteriormente gracias a nuestro ciclo while podremos crear nuestros debidos procesos y anexarlos a las opciones de nuestro menu pricipal
#Si el numero de opcion ingresado por el usuario es el numero 1 se inicia el siguiente proceso.
#Este proceso corresponde a la opcion para agregar un producto.
    if opcion == "1":
        nombre_archivo = input("Ingrese el nombre del archivo: ")
#pediremos al usuario el codigo del producto que desea esto para validar las restricciones que piden las instrucciones.
        codigo_producto = input("Ingrese el código del producto (4 dígitos): ")
        if len(codigo_producto) == 4 and codigo_producto.isdigit():
#Este proceso consiste en tomar el contenido actual del archivo y verificar linea por linea si el codigo que ingreso el usuario
#es nuevo o ya existe dentro del mismo.
            datos_actuales = abrir_archivo(nombre_archivo)
            existe = False
#esta funcion leera liena por linea usando un for
            lineas = datos_actuales.split('\n')
            for linea in lineas:
                partes = linea.split(',')
#esto dividira en partes el codigo para asi hacer su verificacion.
                if len(partes) == 2 and partes[0] == codigo_producto:
                    existe = True
                    break
#si el codigo existe se mostrara el siguiente mensaje, y el programa tendra un reinicio
            if existe:
                print("El código del producto ya existe en el archivo.")
#caso contrario si el codigo es nuevo le pedira al usaurio que ingrese los datos del producto que desea agregar al archivo.
            else:
                descripcion_producto = input("Ingrese la descripción del producto: ")
#guardaremos los datos en "agregar_producto" que es una funcion que creamos al incio de nuestro programa.
                agregar_producto(nombre_archivo, codigo_producto, descripcion_producto)

#Si el usuario ingresa el numero 2 se hara el proceso de (buscar un producto por codigo)
#Y se imprimira lo siguiente
    elif opcion == "2":
#pediremos el nombre del archivo.
        nombre_archivo = input("Ingrese el nombre del archivo: ")
#posteriormente pediremos el codigo para buscar el producto correspondiente al mismo.
        codigo_producto = input("Ingrese el código del producto (4 dígitos): ")
#un codigo correspondiente a 4 digitos
        if len(codigo_producto) == 4 and codigo_producto.isdigit():
#si el codigo ingressado es correcto se mostrar el producto correspondiente al mismo y su descripción del mismo
            buscar_producto(nombre_archivo, codigo_producto)
#caso contrario se mostrara el siguiente mensaje, informando al usuario que el codigo no existe dentro del archivo.
        else:
            print("El código ingresado no existe en nuestros registros.")

#si el usario ingresa el numero 3 correspondiente a "modifcar los datos de algun producto"  se imprimira lo siguiente:
    elif opcion == "3":
#pediremos el nombre del archivo y el programa lo leera.
        nombre_archivo = input("Ingrese el nombre del archivo: ")
#posteriormente pediremos el codigo del producto que este desea modificar.
        codigo_producto = input("Ingrese el código del producto (4 dígitos): ")
#validamos que el codigo debe de constar de 4 numeros
        if len(codigo_producto) == 4 and codigo_producto.isdigit():
#si el codigo es correcto iniciara el proceso de modifcar producto que creamos al inicio de nuestro archivo.
#unicamente reeescribira lo que nosotros modifiquemos.
#el codigo del producto no puede ser modificaado en el programa, si quiere hacerlo debe de hacerlo en el archivo original.
            editar_producto(nombre_archivo, codigo_producto)
#si el codigo no existe se mostrara el siguiente mensaje
        else:
            print("El código ingresado existe en nuestros registros.")
#si el usuario ingresa el numero 4 se imprimira lo sigueinte:
    elif opcion == "4":
#el programa imprima las restricciones con las que cuenta el mismo.
        print("\nCada opción del menú conteniene las siguientes limitantes:\n")
        print("1). Agregar producto: el código de producto no debe repetirse.\n2). Buscar producto: se debe buscar por el código.\n3). Modificar datos: el código no puede modificarse, los otros atributos si\n")
#si el usuario ingresa la opcion de salir, el programa se cerrara.
    elif opcion == "5":
#imprimira el siguiente mensaje para informar al usuario que este saliendo del programa
        print("Cerrando el programa.")
        print("\nEspero haberte ayudado.")
        break
#ya no hay mas codigo ಥ⁠‿⁠ಥ