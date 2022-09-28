"""
A- Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M
B- Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F
C- Recorrer la lista y determinar cuál es el superhéroe más alto de género M 
D- Recorrer la lista y determinar cuál es el superhéroe más alto de género F 
E- Recorrer la lista y determinar cuál es el superhéroe más bajo  de género M 
F- Recorrer la lista y determinar cuál es el superhéroe más bajo  de género F 
G- Recorrer la lista y determinar la altura promedio de los  superhéroes de género M
H- Recorrer la lista y determinar la altura promedio de los  superhéroes de género F
I- Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (ítems C a G)
J- Determinar cuántos superhéroes tienen cada tipo de color de ojos.
K- Determinar cuántos superhéroes tienen cada tipo de color de pelo.
L- Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de no tener, Inicializarlo con ‘No Tiene’). 
M- Listar todos los superhéroes agrupados por color de ojos.
N- Listar todos los superhéroes agrupados por color de pelo.
O- Listar todos los superhéroes agrupados por tipo de inteligencia
"""
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

def mostrar_personaje(personaje:dict):
    """
    Muestra al personaje con todos sus datos ordenados prolijamente
    """
    print("Nombre: {0} \nIdentidad: {1} \nEmpresa: {2} \nAltura: {3} \nPeso: {4} \nGenero: {5} \nColor de ojos: {6} \nColor de pelo: {7} \nFuerza: {8} \nInteligencia: {9}".format(personaje["nombre"], personaje["identidad"], personaje["empresa"], personaje["altura"], personaje["peso"], personaje["genero"], personaje["color_ojos"], personaje["color_pelo"], personaje["fuerza"], personaje["inteligencia"]))

def calcula_maximo_minimo(lista:list, clave:str, tipo:str) -> dict:
    """
    Calcula el maximo o el minimo en base a la  clave recibida

    Recibe una lista de diccionarios y la clave que se utilizara para calcular y 
    el tipo de calculo a realizar

    Devuelve/retorna el  diccionario que contiene el maximo o minimo, o [-1] en caso de ERROR
    """
    retorno = -1
    if(type(lista) == type([]) and type(clave) == type("") and len(lista) > 0):
        maximo_minimo = lista[0]

        for personaje in lista:
            if(tipo == "maximo" and float(personaje[clave]) > float(maximo_minimo[clave])):
                maximo_minimo = personaje #te guardas el diccionario entero

            if(tipo == "minimo" and float(personaje[clave]) < float(maximo_minimo[clave])):
                maximo_minimo = personaje #te guardas el diccionario entero

        retorno = maximo_minimo
    return retorno

def obtener_primer_femenino():
    for personaje in lista_personajes:
        if (personaje["genero"] == "F"):
            return personaje
def obtener_primer_masculino():
    for personaje in lista_personajes:
        if (personaje["genero"] == "M"):
            return personaje

def nombre_personajes_hombres():
    for personaje in lista_personajes:
        if(personaje["genero"] == "M"):
            print(personaje["nombre"])
def nombre_personajes_mujeres():
    for personaje in lista_personajes:
        if(personaje["genero"] == "F"):
            print(personaje["nombre"])




def calcular_personaje_masculino_mas_alto():
#------------------------------MASCULINO MAS ALTO---------------------------------------------------
    """
    personaje_masculino_mayor = obtener_primer_masculino()
    personaje_masculino_mayor["altura"] = float(personaje_masculino_mayor["altura"])

    for personaje in lista_personajes:
        personaje["altura"] = float(personaje["altura"])
        if (personaje["genero"] == "M"):
            if (personaje["altura"] > personaje_masculino_mayor["altura"]):
                personaje_masculino_mayor = personaje
    #print(personaje_masculino_mayor) 
    """
    personaje = calcula_maximo_minimo(lista_personajes,"altura","maximo")
    mostrar_personaje(personaje)
# C- Recorrer la lista y determinar cuál es el superhéroe más alto de género M 
#---------------------------------------------------------------------------------------------------



def calcular_personaje_femenino_mas_alto():
#------------------------------FEMENINO MAS ALTO----------------------------------------------------
    '''
    personaje_femenino_mayor = obtener_primer_femenino()
    personaje_femenino_mayor["altura"] = float(personaje_femenino_mayor["altura"])
    for personaje in lista_personajes:
        personaje["altura"] = float(personaje["altura"])
        if (personaje["genero"] == "F"):
            if (personaje["altura"] > personaje_femenino_mayor["altura"]):
                personaje_femenino_mayor = personaje
    '''

    if(personaje["genero"] == "F"):
        personaje = calcula_maximo_minimo(lista_personajes,"altura","maximo")
        mostrar_personaje(personaje)
# D- Recorrer la lista y determinar cuál es el superhéroe más alto de género F 
#---------------------------------------------------------------------------------------------------



def calcular_personaje_masculino_mas_bajo():
#------------------------------MASCULINO MAS BAJO---------------------------------------------------
    '''
    personaje_masculino_menor = obtener_primer_masculino()
    personaje_masculino_menor["altura"] = float(personaje_masculino_menor["altura"])
    for personaje in lista_personajes:
        personaje["altura"] = float(personaje["altura"])
        if (personaje["genero"] == "M"):
            if (personaje["altura"] < personaje_masculino_menor["altura"]):
                personaje_masculino_menor= personaje
    '''
    personaje = calcula_maximo_minimo(lista_personajes,"altura","minimo")
    mostrar_personaje(personaje)
# E- Recorrer la lista y determinar cuál es el superhéroe más bajo  de género M 
#---------------------------------------------------------------------------------------------------



def calcular_personaje_femenino_mas_bajo():
#------------------------------FEMENINO MAS BAJO----------------------------------------------------
    '''
    personaje_femenino_menor = obtener_primer_femenino()
    personaje_femenino_menor["altura"] = float(personaje_femenino_menor["altura"])
    for personaje in lista_personajes:
        personaje["altura"] = float(personaje["altura"])
        if (personaje["genero"] == "F"):
            if (personaje["altura"] < personaje_femenino_menor["altura"]):
                personaje_femenino_menor["altura"] = personaje["altura"]
    '''
    personaje = calcula_maximo_minimo(lista_personajes,"altura","minimo")
    mostrar_personaje(personaje)
# F- Recorrer la lista y determinar cuál es el superhéroe más bajo  de género F 
#---------------------------------------------------------------------------------------------------




def calcular_promedio_altura_personajes_masculinos():
#------------------------------PROMEDIO ALTURA MASCULINO--------------------------------------------
    acumulador_altura_masculino = 0
    cantidad_personajes_masculino = 0
    for personaje in lista_personajes:
        if(personaje["genero"] == "M"):
            acumulador_altura_masculino = acumulador_altura_masculino + float(personaje["altura"])
            cantidad_personajes_masculino += 1

    promedio_altura_masculino = acumulador_altura_masculino / cantidad_personajes_masculino
    print(promedio_altura_masculino)
#G- Recorrer la lista y determinar la altura promedio de los  superhéroes de género M
#---------------------------------------------------------------------------------------------------



def calcular_promedio_altura_personajes_femeninos():
#------------------------------PROMEDIO ALTURA FEMENINO---------------------------------------------
    acumulador_altura_femenino = 0
    cantidad_personajes_femenino = 0
    for personaje in lista_personajes:
        if (personaje["genero"] == "F"):
            acumulador_altura_femenino = acumulador_altura_femenino + float(personaje["altura"])
            cantidad_personajes_femenino += 1
    
    promedio_altura_femenino = acumulador_altura_femenino / cantidad_personajes_femenino
    print(promedio_altura_femenino)
#H- Recorrer la lista y determinar la altura promedio de los  superhéroes de género #---------------------------------------------------------------------------------------------------



def calcular_nombres_de_anteriores():
#------------------------------CALCULA SOLO NOMBRES DE ANTERIORES FUNCIONES-------------------------
    masculino_mas_alto = calcular_personaje_masculino_mas_alto()
    print("El nombre del masculino mas alto es: {0}" .format(masculino_mas_alto["nombre"]))

    femenino_mas_alto = calcular_personaje_femenino_mas_alto()
    print("El nombre del femenino mas alto es: {0}" .format(femenino_mas_alto["nombre"]))


    masculino_mas_bajo = calcular_personaje_masculino_mas_bajo()
    print("El nombre del masculino mas bajo es: {0}" .format(masculino_mas_bajo["nombre"]))

    femenino_mas_bajo = calcular_personaje_femenino_mas_bajo()
    print("El nombre del femenino mas bajo es: {0}" .format(femenino_mas_bajo["nombre"]))
#I- Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (ítems C a F)
#---------------------------------------------------------------------------------------------------



def calcular_tipo_color_ojos_personajes():
#------------------------------TIPO DE OJOS---------------------------------------------------------
    tipo_color_de_ojos = {}
    for personaje in lista_personajes:
        tipo_color_de_ojos[personaje["color_ojos"]] = 0

    for personaje in lista_personajes:
        tipo_color_de_ojos[personaje["color_ojos"]] += 1
        
    print(tipo_color_de_ojos)
#J- Determinar cuántos superhéroes tienen cada tipo de color de ojos.
#---------------------------------------------------------------------------------------------------



def calcular_tipo_color_pelo_personajes():
#------------------------------TIPO DE PELO---------------------------------------------------------
    tipo_color_de_pelo = {}
    for personaje in lista_personajes:
        tipo_color_de_pelo[personaje["color_pelo"]] = 0
    
    for personaje in lista_personajes:
        tipo_color_de_pelo[personaje["color_pelo"]] += 1
    
    print(tipo_color_de_pelo)
# K- Determinar cuántos superhéroes tienen cada tipo de color de pelo.
#---------------------------------------------------------------------------------------------------



def calcular_tipo_inteligencia_personajes():
#------------------------------TIPO DE INTELIGENCIA--------------------------------------------------
    tipo_de_inteligencia = {}
    for personaje in lista_personajes:
        if (personaje["inteligencia"] == ""):
            tipo_de_inteligencia["No tiene"] = 0
        else:   
            tipo_de_inteligencia[personaje["inteligencia"]] = 0

    for personaje in lista_personajes:
        if (personaje["inteligencia"] == ""):
            tipo_de_inteligencia["No tiene"] += 1
        else:
            tipo_de_inteligencia[personaje["inteligencia"]] += 1

    print(tipo_de_inteligencia)
# L- Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de no tener, Inicializarlo con ‘No Tiene’).
#--------------------------------------------------------------------------------------------------- 



def calcular_personajes_agrupados_color_ojos():
#------------------------------COLOR DE OJOS AGRUPADOS----------------------------------------------
    dic_color_ojos = {}

    # dic_color_ojos = {}
    # dic_color-ojos = {"azul": []}
    # dic_color_ojos = {"azul": ["capitan america", "spiderman"]}

    for personaje in lista_personajes:

        personaje["color_ojos"] = personaje["color_ojos"].lower()
        color_ojos = personaje["color_ojos"]
        dic_color_ojos[color_ojos] = []

    for personaje in lista_personajes:
        for color in dic_color_ojos:

            color_ojos = personaje["color_ojos"]
            if (color_ojos == color):
                dic_color_ojos[color].append(personaje["nombre"])
        
    print(dic_color_ojos)
# M- Listar todos los superhéroes agrupados por color de ojos.
#---------------------------------------------------------------------------------------------------



def calcular_personajes_agrupados_color_pelo():
#------------------------------COLOR DE PELO AGRUPADOS----------------------------------------------
    dic_color_pelo = {}

    for personaje  in lista_personajes:

        personaje["color_pelo"] = personaje["color_pelo"].lower()
        color_pelo = personaje["color_pelo"]
        dic_color_pelo[color_pelo] = []

    for personaje in lista_personajes:
        for color in dic_color_pelo:

            color_pelo = personaje["color_pelo"]
            if(color == color_pelo):
                dic_color_pelo[color].append(personaje["nombre"])
    
    print(dic_color_pelo)
# N- Listar todos los superhéroes agrupados por color de pelo.
#---------------------------------------------------------------------------------------------------



def calcular_personajes_agrupados_tipo_de_inteligencia():
#------------------------------AGRUPADOS POR INTELIGENCIA-------------------------------------------
    dic_tipo_inteligencia = {}

    for personaje in lista_personajes:
        
        personaje["inteligencia"] = personaje["inteligencia"].lower()
        tipo_inteligencia = personaje["inteligencia"]
        dic_tipo_inteligencia[tipo_inteligencia] = []

    for personaje in lista_personajes:
        for inteligencia in dic_tipo_inteligencia:

            tipo_inteligencia = personaje["inteligencia"]
            if(inteligencia == tipo_inteligencia):
                dic_tipo_inteligencia[inteligencia].append(personaje["nombre"])

    print(dic_tipo_inteligencia)
# O- Listar todos los superhéroes agrupados por tipo de inteligencia
#---------------------------------------------------------------------------------------------------



while True:
    
    respuesta = input("\n 1- Nombre personajes hombres \n 2- Nombre personajes mujeres \n 3- Personaje masculino mas alto \n 4- Personaje femenino mas alto \n 5- Personaje femenino mas bajo \n 6- Personaje masculino mas bajo \n 7- Promedio altura masculinos \n 8- Promedio altura femeninos \n 9- calcular el nombre de lo anterior \n 10- Calcular tipo de ojos de los personajes \n 11- Calcular tipo de pelo de los personajes \n 12- Calcular tipo de inteligencia de los personajes \n 13- Calcular personajes agrupados por color de ojos \n 14- Calcular personajes  agrupados por color de pelo \n 15- Calcular personajes agrupados por tipo de inteligencia \n 16- Para salir \n Que desea saber? ")

    if (respuesta == "1"):
        nombre_personajes_hombres()
    elif (respuesta == "2"):
        nombre_personajes_mujeres()
    elif (respuesta == "3"):
        calcular_personaje_masculino_mas_alto()
    elif (respuesta == "4"):
        calcular_personaje_femenino_mas_alto()
    elif (respuesta == "5"):
        calcular_personaje_femenino_mas_bajo()
    elif (respuesta == "6"):
        calcular_personaje_masculino_mas_bajo()
    elif (respuesta == "7"):
        calcular_promedio_altura_personajes_masculinos()
    elif (respuesta == "8"):
        calcular_promedio_altura_personajes_femeninos()
    elif (respuesta == "9"):
        calcular_nombres_de_anteriores()
    elif (respuesta == "10"):
        calcular_tipo_color_ojos_personajes()
    elif (respuesta == "11"):
        calcular_tipo_color_pelo_personajes()
    elif (respuesta == "12"):
        calcular_tipo_inteligencia_personajes()
    elif (respuesta == "13"):
        calcular_personajes_agrupados_color_ojos()
    elif (respuesta == "14"):
        calcular_personajes_agrupados_color_pelo()
    elif (respuesta == "15"):
        calcular_personajes_agrupados_tipo_de_inteligencia()
    elif (respuesta == "16"):
        break

