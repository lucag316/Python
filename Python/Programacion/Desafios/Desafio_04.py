from data_stark import lista_personajes
import re 

def extraer_iniciales(nombre_heroe:str)->str:
    '''
    Recibe por parametro un string con el nombre del personaje

    Devuelve las iniciales del nombre del personaje
    '''

    retorno = "N/A"
    iniciales = ""

    if(type(nombre_heroe) == type("") and len(nombre_heroe) > 0):
        nombre_heroe = nombre_heroe.upper()
        nombre_heroe = nombre_heroe.replace("THE ", "")
        nombre_heroe = nombre_heroe.replace("-", " ")
        nombre_heroe = nombre_heroe.strip()
        partes_nombre = nombre_heroe.split(" ")

        for una_parte in partes_nombre:
            iniciales += una_parte[0] + "."
    
        retorno = iniciales

    return retorno
#------------------------------------------------1.1----------------------------------------------------------------------
#print(extraer_iniciales("howard the duck"))

def definir_iniciales_nombre(heroe:dict)->dict:
    '''
    Recibe por parametro el diccionario con la informacion del personaje

    La funcion agrega una clave al diccionario que contiene las iniciales del personaje

    Devuelve un diccionario

    '''
    retorno = False
    if(type(heroe) == type(dict())):
        heroe["iniciales"] = extraer_iniciales(heroe["nombre"]) #agrego la clave al  diccionario
        retorno = True

#   print(heroe)
    return retorno
#-------------------------------------------1.2---------------------------------------------------------------------
#print(definir_iniciales_nombre(lista_personajes[0]))

def agregar_iniciales_nombre(lista_heroes:list):
    '''
    
    '''
    if(type(lista_heroes) == type([]) and len(lista_heroes) > 0):
        for heroe in lista_heroes:
            if(definir_iniciales_nombre(heroe) == False):
                print("El origen de datos no contiene el formato correcto")
                retorno = False 
            else:
                retorno = True
    return retorno
#----------------------------------------1.3------------------------------------------------------
#agregar_iniciales_nombre(lista_personajes)

def stark_imprimir_nombres_con_iniciales(lista_heroes:list):
    if(type(lista_heroes) == type([]) and len(lista_heroes) > 0):
        agregar_iniciales_nombre(lista_heroes)

        for heroe in lista_heroes:
            nombre_heroe = heroe["nombre"]
            iniciales_heroe = heroe["iniciales"]

            print("* {0} ({1}) ".format(nombre_heroe, iniciales_heroe))
#-------------------------------------1.3------------------------------------------------------------------------
#stark_imprimir_nombres_con_iniciales(lista_personajes)

def generar_codigo_heroe(id_heroe:int, genero_heroe:str):
    '''
    Recibe el id_heroe (un entero) cualquier entero en esta funcion
    Recibe el genero del heroe (M), (F), (NB)
    '''
    retorno = "N/A"

    if(type(id_heroe) == type(int()) and genero_heroe != ""):
        if(genero_heroe == "F" or genero_heroe == "M" or genero_heroe == "NB"):
            relleno = 10 - (len(genero_heroe) + 1)
            id_heroe_str = str(id_heroe).zfill(relleno)

            retorno = "{0}-{1}".format(genero_heroe, id_heroe_str)
            
    return retorno
#--------------------------------------------2.1-------------------------------------------------------------------
#print(generar_codigo_heroe(4654,"M"))

def agregar_codigo_heroe(heroe:dict, id_heroe:int):
    '''
    heroe: un diccionario con los datos del personaje
    id_heroe: un entero que representa el identificador del héroe.
    '''
    retorno = False
    if(heroe != ""):
        codigo_heroe = generar_codigo_heroe(id_heroe, heroe["genero"])

        if(len(codigo_heroe) == 10):

            heroe["codigo_heroe"] =  codigo_heroe
            retorno = True

    return retorno
#---------------------------------------2.2----------------------------------------------------------------
#print(agregar_codigo_heroe(lista_personajes[0], 64645))

def stark_generar_codigos_heroes(lista_heroes:list):

    contador = 0

    if(len(lista_heroes) > 0):

        for heroe in lista_heroes:

            if(type(heroe) == type(dict())):# falta validar Todos los elementos contengan la clave ‘genero’

                contador += 1
                agregar_codigo_heroe(heroe, contador)
                print("* El codigo del heroe es: {0} ".format(heroe["codigo_heroe"]))

        print("se asignaron {0} codigos ".format(contador))
#       print("El codigo del primer heroe es: {0} ".format(lista_personajes[0]["codigo_heroe"]))
#       print("El codigo del ultimo heroe es: {0} ".format(lista_personajes[-1]["codigo_heroe"]))
    else:
        print("El origen de datos no contiene el formato correcto")
#---------------------------------------------2.3-----------------------------------------------------------
#stark_generar_codigos_heroes(lista_personajes)

def sanitizar_entero(numero_str:str):
    '''
    Recibe un string que representa un posible número entero
    '''
    encontar_numero_str = re.findall("[a-zA-Z]", numero_str)

    if(len(encontar_numero_str) == 0):

        encontar_numero_str = re.findall("^[+-]?[0-9]+$", numero_str)
        numero_str = numero_str.strip()

        if(len(encontar_numero_str) == 1):
            numero_str = int(numero_str)

            if(type(numero_str) == type(int())):

                if(numero_str > 0):
                    retorno = numero_str
                else:
                    retorno = -2
        else:
            retorno = -3
    else:
        retorno = -1

    return retorno
#--------------------------------------------3.1-----------------------------------------------------------
#print(sanitizar_entero("-26"))

def sanitizar_flotante(numero_str:str):

    encontar_numero_str = re.findall("[a-zA-Z]", numero_str)

    if(len(encontar_numero_str) == 0):

        encontar_numero_str = re.findall("^[+-]?[0-9]+$", numero_str)
        numero_str = numero_str.strip()

        if(len(encontar_numero_str) == 1):
            numero_str = float(numero_str)

            if(type(numero_str) == type(float())):

                if(numero_str > 0):
                    retorno = numero_str
                else:
                    retorno = -2
        else:
            retorno = -3
    else:
        retorno = -1

    return retorno
#--------------------------------------------3.2---------------------------------------------------------------------
#print(sanitizar_flotante("45"))


def sanitizar_string(valor_str:str, valor_por_defecto:str):
    '''
    valor_str: un string que representa el texto a validar
    valor_por_defecto: un string que representa un valor por defecto (parámetro opcional, inicializarlo con ‘-’)
    '''
    encontar_numero_str = re.findall("[a-zA-Z]", numero_str)

    if(len(encontar_numero_str) == 0):

        encontar_numero_str = re.findall("^[+-]?[0-9]+$", numero_str)
        numero_str = numero_str.strip()

        if(len(encontar_numero_str) == 1):
            numero_str = float(numero_str)

            if(type(numero_str) == type(float())):

                if(numero_str > 0):
                    retorno = numero_str
                else:
                    retorno = -2
        else:
            retorno = -3
    else:
        retorno = -1

    return retorno
#--------------------------------------------------3.3-----------------------------------------------------------------




# La función deberá analizar el string recibido y determinar si es solo texto (sin números). En caso de encontrarse números retornar “N/A”
# En el caso que valor_str contenga una barra ‘/’ deberá ser reemplazada por un espacio
# 	El espacio es un caracter válido 
# En caso que se verifique que el parámetro recibido es solo texto, se deberá retornar el mismo convertido todo a minúsculas
# En el caso que el texto a validar se encuentre vacío y que nos hayan pasado un valor por defecto, entonces retornar el valor por defecto convertido a minúsculas
# Quitar los espacios en blanco de atras y adelante de ambos parámetros en caso que los tuviese
