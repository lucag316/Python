from data_stark import lista_personajes
"""
 {
    "nombre": "Howard the Duck",
    "identidad": "Howard (Last name unrevealed)",
    "empresa": "Marvel Comics",
    "altura": "79.349999999999994",
    "peso": "18.449999999999999",
    "genero": "M",
    "color_ojos": "Brown",
    "color_pelo": "Yellow",
    "fuerza": "2",
    "inteligencia": ""
  }
  """

def stark_normalizar_datos(lista_heroes:list, clave:str):
    '''
    Normaliza los datos en base a la clave recibida

    Recibe una lista de diccionarios

    Devuelve los datos normalizados en su tipo correspondiente
    '''
    flag_datos_normalizados = False
    for personaje in lista_heroes:
        if(clave == "altura" or clave == "peso"):
            if(type(personaje[clave]) == type(str())):
                personaje[clave] = float(personaje[clave])
                flag_datos_normalizados = True

        if(clave == "fuerza"):
            if(type(personaje[clave]) == type(str())):
                personaje[clave] = float(personaje[clave])
                flag_datos_normalizados = True

    if(flag_datos_normalizados == True):
        print("Datos normalizados")

    if(lista_heroes == 0):
        print("Error: Lista de héroes vacía")
#-------------------------------------------0----------------------------------------------------
def obtener_nombre(heroe:dict) -> str:
    '''
    Recibe por parametro un diccionario

    Devuelve un string con su nombre formateado
    '''
    nombre_heroe = heroe["nombre"]
    mensaje = "Nombre: {0} ".format(nombre_heroe)
    return mensaje
#-----------------------------------------1.1--------------------------------------------------------------------
def imprimir_dato(dato:str):
    '''
    Imprime un dato

    Recibe una string

    Imprime el dato en la  consola
    '''
    print(dato)
#---------------------------------------1.2--------------------------------------------------------------------
def stark_imprimir_nombres_heroes(lista_heroes:list):
 
    if(len(lista_heroes) > 0):
        for heroe in lista_heroes:
            print(obtener_nombre(heroe))
    
    elif(len(lista_heroes) == 0):
        return imprimir_dato("-1")
#------------------------------------------1.3-----------------------------------------------------------------------
def obtener_nombre_y_dato(heroe:dict, key:str) -> str:
    '''
    Recibe por parametro un diccionario y una key que es el dato que desea obtener

    Devuelve un string con el nombre y el dato (key)
    '''
    nombre = obtener_nombre(heroe)
    dato_heroe = heroe[key]

    mensaje = print(" {0} | {1}: {2}".format(nombre, key, dato_heroe))
    return mensaje
#-------------------------------------------2.0-------------------------------------------------------------
#obtener_nombre_y_dato(lista_personajes[0], "altura")
def stark_imprimir_nombres_alturas(lista_heroes:list):
    '''
    Recibe por parametro la lista de heroes

    Devuelve los nombres y las alturas
    '''
    if(len(lista_heroes) == 0):
        datos_heroe = -1
    elif(len(lista_heroes) > 0):
        for heroe in lista_heroes:
            datos_heroe = obtener_nombre_y_dato(heroe, "altura")
        
    return datos_heroe
#----------------------------------------------3----------------------------------------------
#print(stark_imprimir_nombres_alturas(lista_personajes))
def calcular_max(lista_heroes:list, clave:str):
    '''
    Recibe por parametro la lista de heroes y la clave que representa el dato a ser evaluado

    determina el maximo de la lista
    '''
    if(type(lista_heroes) == type([]) and type(clave) == type("")):
        maximo = lista_heroes[0]
        for heroe in lista_heroes:
            if(float(heroe[clave]) > float(maximo[clave])):
                maximo = heroe

    return maximo
#-------------------------------------4.1--------------------------------------------------
#print(calcular_max(lista_personajes,"altura"))
def calcular_min(lista_heroes:list, clave:str):
    '''
    Recibe por parametro la lista de heroes y la clave que representa el dato a ser evaluado

    determina el minimo de la lista
    '''
    if(type(lista_heroes) == type([]) and type(clave) == type("")):
        minimo = lista_heroes[0]
        for heroe in lista_heroes:
            if(float(heroe[clave]) < float(minimo[clave])):
                minimo = heroe

    return minimo
#-------------------------------------4.2------------------------------------------------------
#print(calcular_min(lista_personajes,"peso"))
def calcular_max_min_dato(lista_heroes:list, tipo:str, clave:str):
    '''
    Recibe 3 parametros: la lista de heroes, la key, y el tipo(maximo o minimo)

    Retorna al heroe que cumpla con la condicion pedida
    '''
    if(tipo == "maximo"):
        heroe = calcular_max(lista_heroes,clave)
    else:
        heroe = calcular_min(lista_heroes,clave)
        
    return heroe
#-----------------------------------4.3-------------------------------------------------
#print(calcular_max_min_dato(lista_personajes,"maximo", "peso"))
def stark_calcular_imprimir_heroe(lista_heroes:list, tipo:str, clave:str):
    if(len(lista_heroes) == 0):
        datos_heroe = -1
    elif(len(lista_heroes) > 0):
            datos_heroe = calcular_max_min_dato(lista_heroes, tipo, clave)
            datos_heroe = obtener_nombre_y_dato(datos_heroe, clave)
    imprimir_dato(datos_heroe)
#-------------------------------------4.4------------------------------------------------------------
#stark_calcular_imprimir_heroe(lista_personajes, "maximo", "peso")
def sumar_dato_heroe(lista_heroes:list, key:str):
    suma = 0
    for heroe in lista_heroes:
        if(type(heroe) != type(dict()) or heroe == ""):
            suma = -1
        else:
            suma += float(heroe[key])

    return suma
#------------------------------------5.1----------------------------------------------------------
#print(sumar_dato_heroe(lista_personajes, "fuerza"))
def dividir(dividendo:int, divisor:int):
    if(divisor == 0):
        resultado = 0
    else:
        resultado = dividendo / divisor

    return resultado
#-------------------------------------------5.2-------------------------------------------------------
#print(dividir(2000, 1000))
def calcular_promedio(lista_heroes:list, clave:str):
    cantidad_heroes = len(lista_heroes)
   # print(cantidad_heroes)
    suma = sumar_dato_heroe(lista_heroes, clave)
    promedio = dividir(suma, cantidad_heroes)
    return promedio
#-------------------------------------------5.3------------------------------------------------------------
#print(calcular_promedio(lista_personajes, "peso"))  #estaria bueno hacer el mensaje mas lindo, con solo dos numeros despues de la coma
def stark_calcular_imprimir_promedio_altura(lista_heroes:list):
    if(lista_heroes == ""):
        altura_promedio = -1
    else:
        altura_promedio = calcular_promedio(lista_heroes, "altura")

    imprimir_dato(altura_promedio)
#------------------------------------------5.4-------------------------------------------------------------------
#stark_calcular_imprimir_promedio_altura(lista_personajes)
# IMPORTANTE: hacer uso de las las funciones creadas en los puntos 1.2, 5.1 y 5.3
def imprimir_menu():
    while True:
        menu = input("1- Obtener nombres de los personajes \n2- Obtener nombres y alturas \n3- Calcular personaje mas alto \n4- Calcular personaje mas bajo \n5- Calcular personaje mas pesado \n6- Calcular personaje menos pesado \n7- Calcular personaje mas fuerte \n8- Calcular personaje menos fuerte \n9- Calcular premedio peso \n10- Calcular promedio fuerza \n11- Calcular promedio altura \n12- Salir \nQue desea saber? ")
        if(menu == "1"):
            stark_imprimir_nombres_heroes(lista_personajes)
        elif(menu == "2"):
            stark_imprimir_nombres_alturas(lista_personajes)
        elif(menu == "3"):
            stark_calcular_imprimir_heroe(lista_personajes, "maximo", "altura")
        elif(menu == "4"):
            stark_calcular_imprimir_heroe(lista_personajes, "minimo", "altura")
        elif(menu == "5"):
            stark_calcular_imprimir_heroe(lista_personajes, "maximo", "peso")
        elif(menu == "6"):
            stark_calcular_imprimir_heroe(lista_personajes, "minimo", "peso")
        elif(menu == "7"):
            stark_calcular_imprimir_heroe(lista_personajes, "maximo", "fuerza")
        elif(menu == "8"):
            stark_calcular_imprimir_heroe(lista_personajes, "minimo", "fuerza")  
        elif(menu == "9"):
            print(calcular_promedio(lista_personajes, "peso"))
            #calcular_promedio(lista_personajes, "peso")
        elif(menu == "10"):
            print(calcular_promedio(lista_personajes, "fuerza"))
        elif(menu == "11"):
            stark_calcular_imprimir_promedio_altura(lista_personajes)  
        elif(menu == "12"):
            break

    imprimir_dato(menu)

#imprimir_menu()
#--------------------------------------------6.1--------------------------------------------------------------------
def validar_entero(numero:str):
    '''
    Recibe un numero en forma de string

    Si es un string conformado de solo difitos retorna True, caso contrario retorna False
    '''
    if(type(numero) == type("")):
        numero = int(numero)
        if(numero == int):
            retorno = True
        else:
            retorno = False

    return retorno
print(validar_entero("74867"))

#-----------------------------------------6.2----------------------------------------------------------------------
# 6.2 Crear la función “validar_entero” la cual recibirá por parámetro un string de número el cual deberá verificar que sea un string conformado únicamente por dígitos. Retornara True en caso de serlo, False caso contrario


def stark_menu_principal():
    
    pass
#------------------------------------------6.3------------------------------------------------------------------------
# 6.3 Crear la función 'stark_menu_principal' la cual se encargará de imprimir el menú de opciones y le pedirá al usuario que ingrese el número de una de las opciones elegidas y deberá validarlo. En caso de ser correcto dicho número, lo retornara casteado a entero, caso contrario retorna -1. Reutilizar las funciones del ejercicio 6.1 y 6.2



def stark_marvel_app():
    pass
#----------------------------------------------7------------------------------------------------------------------
# 7  Crear la función 'stark_marvel_app' la cual recibirá por parámetro la lista de héroes y se encargará de la ejecución principal de nuestro programa. 
# Utilizar if/elif o match según prefiera (match solo para los que cuentan con python 3.10+). Debe informar por consola en caso de seleccionar una opción incorrecta y volver a pedir el dato al usuario. Reutilizar las funciones con prefijo 'stark_' donde crea correspondiente.




