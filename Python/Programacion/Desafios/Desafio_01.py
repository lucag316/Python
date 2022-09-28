# A- Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M
# B- Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F
# C- Recorrer la lista y determinar cuál es el superhéroe más alto de género M 
# D- Recorrer la lista y determinar cuál es el superhéroe más alto de género F 
# E- Recorrer la lista y determinar cuál es el superhéroe más bajo  de género M 
# F- Recorrer la lista y determinar cuál es el superhéroe más bajo  de género F 
# G- Recorrer la lista y determinar la altura promedio de los  superhéroes de género M
# H- Recorrer la lista y determinar la altura promedio de los  superhéroes de género F
# I- Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (ítems C a G)
# J- Determinar cuántos superhéroes tienen cada tipo de color de ojos.
# K- Determinar cuántos superhéroes tienen cada tipo de color de pelo.
# L- Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de no tener, Inicializarlo con ‘No Tiene’). 
# M- Listar todos los superhéroes agrupados por color de ojos.
# N- Listar todos los superhéroes agrupados por color de pelo.
# O- Listar todos los superhéroes agrupados por tipo de inteligencia
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
from data_stark import lista_personajes

def mostrar_personaje(personaje:dict)->dict:
    '''
    Muestra al personaje con todos sus datos ordenados prolijamente
    '''
    print("Nombre: {0} \nIdentidad: {1} \nEmpresa: {2} \nAltura: {3} \nPeso: {4} \nGenero: {5} \nColor de ojos: {6} \nColor de pelo: {7} \nFuerza: {8} \nInteligencia: {9}".format(personaje["nombre"], personaje["identidad"], personaje["empresa"], personaje["altura"], personaje["peso"], personaje["genero"], personaje["color_ojos"], personaje["color_pelo"], personaje["fuerza"], personaje["inteligencia"]))

def obtener_nombres_masculinos():
    for personaje  in lista_personajes:
        if(personaje["genero"] == "M"):
            nombre_personaje = personaje["nombre"]
            print("Nombre: {0} ".format(nombre_personaje))

'''
def obtener_nombres_masculinos(lista_personajes:list):
    for personaje  in lista_personajes:
        if(personaje["genero"] == "M"):
            nombre_personaje = personaje["nombre"]
            print("Nombre: {0} ".format(nombre_personaje))
'''


def obtener_nombres_femeninos():

    for personaje  in lista_personajes:
        if(personaje["genero"] == "F"):
            nombre_personaje = personaje["nombre"]
            print("Nombre: {0} ".format(nombre_personaje))

def calcular_maximo_minimo(lista:list, clave:str, tipo:str)-> dict:
    """
    Calcula el maximo o el minimo en base a la  clave recibida

    Recibe una lista de diccionarios y la clave que se utilizara para calcular y 
    el tipo de calculo a realizar

    Devuelve/retorna el  diccionario que contiene el maximo o minimo, o [-1] en caso de ERROR
    """

    retorno = -1

    if(type(lista) == type([]) and type(clave) == type(str()) and len(lista) > 0):
        maximo_minimo = lista[0]

        for personaje in lista:
            if(tipo == "maximo" and float(personaje[clave]) > float(maximo_minimo[clave])):
                maximo_minimo = personaje

            if(tipo == "minimo" and float(personaje[clave]) < float(maximo_minimo[clave])):
                maximo_minimo = personaje #te guardas el diccionario entero

        retorno = maximo_minimo

    return retorno
    

def calcula_masculino_mas_alto(lista_personajes:list):
#    if(personaje["genero"] == "M"):
    heroe_elejido = calcular_maximo_minimo(lista_personajes, "altura", "maximo")
    return heroe_elejido
                 


def calcula_femenino_mas_alto(lista_personajes:list):
    
    for personaje in lista_personajes:
        calcular_maximo_minimo(lista_personajes,"altura", "maximo")
        if(personaje["genero"] == "F"):
            return mostrar_personaje(personaje)

    
def calcula_masculino_mas_bajo():
    for personaje in lista_personajes:
        if(personaje["genero"] == "M"):
            calcular_maximo_minimo(lista_personajes,"altura", "minimo")       
            return mostrar_personaje(personaje)

def calcula_femenino_mas_bajo():
    for personaje in lista_personajes:
        if(personaje["genero"] == "F"):
            calcular_maximo_minimo(lista_personajes,"altura", "minimo")       
            return mostrar_personaje(personaje)

def promedio_altura_masculino():
    acumulador_alturas = 0
    cantidad_personajes = 0
    for personaje in lista_personajes:
        acumulador_alturas += float(personaje["altura"])
        cantidad_personajes += 1

    promedio_masculino = acumulador_alturas / cantidad_personajes

    return promedio_masculino

def promedio_altura_femenino():
    pass

# I- Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (ítems C a G)

#print(calcular_maximo_minimo(lista_personajes, "altura", "maximo"))

while True:
    respuesta = input("1- obtener_nombres_masculinos \n2- obtener_nombres_femeninos \n3- calcula_masculino_mas_alto \n4- calcula_femenino_mas_alto \n5- calcula_masculino_mas_bajo \n6- calcula_femenino_mas_bajo \n7- promedio_altura_masculino \n8- promedio_altura_femenino \nQue desea saber? ")
    
    if(respuesta == "1"):
        obtener_nombres_masculinos()
    elif(respuesta == "2"):
        obtener_nombres_femeninos()
    elif(respuesta == "3"):
        calcula_masculino_mas_alto(lista_personajes)
    elif(respuesta == "4"):
        calcula_femenino_mas_alto(lista_personajes)
    elif(respuesta == "5"):
        calcula_masculino_mas_bajo()
    elif(respuesta == "6"):
        calcula_femenino_mas_bajo()
    elif(respuesta == "7"):
        promedio_altura_masculino()
    elif(respuesta == "8"):
        promedio_altura_femenino()
    elif(respuesta == "10"):
        break
