# 1-  Listar los primeros N héroes. El valor de N será ingresado por el usuario  (Validar que no supere max. de lista)

# 2-  Ordenar y Listar héroes por altura. Preguntar al usuario si lo quiere ordenar de manera ascendente (‘asc’) o descendente (‘desc’)

# 3-  Ordenar y Listar héroes por fuerza. Preguntar al usuario si lo quiere ordenar de manera ascendente (‘asc’) o descendente (‘desc’)

# 4-  Calcular promedio de cualquier key numérica, filtrar los que cumplan con la condición de superar o no el promedio (preguntar al usuario la condición: ‘menor’ o ‘mayor’) se deberá listar en consola aquellos que cumplan con ser mayores o menores según corresponda.

#  5-  Buscar héroes por inteligencia [good, average, high] y listar en consola los que cumplan dicha búsqueda.

# 6-  Exportar a CSV la lista de héroes ordenada según opción elegida anteriormente [1-4]

'''
Los puntos deben ser accedidos mediante un menú. Para todas las opciones, validar lo ingresado por consola con RegEx
El set de datos proviene de un json
Realizar las validaciones que crea pertinentes
En todos los casos se deberá trabajar con una copia de la lista original

'''
import re
import json

url_archivo = r"C:\Users\luca_\Desktop\programacion_1b\preparcial\data_stark.json"

def abrir_archivo():
    with open(url_archivo,"r") as archivo:
        data = json.load(archivo)

    return data["heroes"]
#print(abrir_archivo())

def validar_entero(numero_str:str)->int:
    result = re.match("^[0-9]+$",numero_str)
    if(result != None):
        return int(numero_str)
    else:
        return False

def listar_heroes(lista_heroes:list):
    '''
    Recibe la lista de personajes y un numero de los primeros N heroes

    Devuelve la lista con esos N primeros personajes
    '''
    numero_heroes = input("Ingrese el numero de los primeros N heroes ")
    numero_heroes = validar_entero(numero_heroes)

    if(numero_heroes != False):
        if(numero_heroes > len(lista_heroes)):
            print("ERROR, mayor a la cantidad de heroes")
            numero_heroes = len(lista_heroes)

        for i in range(numero_heroes):
            print(lista_heroes[i])

    else:
        print("Numero no valido ")
#--------------------------------------------1----------------------------------------------------------------
lista_personajes = abrir_archivo()
#listar_heroes(lista_personajes)

def buscar_maximo(lista_maximo:list, key:str):
    maximo = 0
    for i in range(len(lista_maximo)):
        if(lista_maximo[i][key] > lista_maximo[maximo][key]):
            maximo = i

    return maximo
def buscar_minimo(lista_minimo:list, key:str):
    minimo = 0
    for i in range(len(lista_minimo)):
        if(lista_minimo[i][key] < lista_minimo[minimo][key]):
            minimo = i
            
    return minimo

def ordenar_listar_heroes_altura(lista_heroes_desordenada:list)->list:
    '''
    Recibe la lista de heroes

    Devuelve la ordenada segun la altura, de manera ascendente o descendente segun el usuario quiera
    '''
    manera_a_ordenar = input("La quiere ordenar de manera ascendente(asc) o de manera descendente(desc)? ")
    lista_heroes_copiada = lista_heroes_desordenada.copy()
    lista_heroes_ordenada = []

    while len(lista_heroes_copiada) > 0:
        if(manera_a_ordenar == "desc"):
            indice_maximo = buscar_maximo(lista_heroes_copiada,"altura")
            elemento_maximo = lista_heroes_copiada.pop(indice_maximo)
            lista_heroes_ordenada.append(elemento_maximo)
        elif(manera_a_ordenar == "asc"):
            indice_minimo = buscar_minimo(lista_heroes_copiada,"altura")
            elemento_minimo = lista_heroes_copiada.pop(indice_minimo)
            lista_heroes_ordenada.append(elemento_minimo)
        else:
            print("ERROR, no existe el tipo de orden")
            break
    mensaje = ""
    for heroe in lista_heroes_ordenada:
        nombre_heroe = heroe["nombre"]
        altura_heroe = heroe["altura"]
        mensaje += "Nombre: {0}    Altura: {1} \n".format(nombre_heroe, altura_heroe)
        
    return mensaje
#-----------------------------------------2-----------------------------------------------------
#print(ordenar_listar_heroes_altura(lista_personajes))

def ordenar_listar_heroes_fuerza(lista_heroes_desordenada:list)->list:
    '''
    Recibe la lista de heroes

    Devuelve la ordenada segun la fuerza, de manera ascendente o descendente segun el usuario quiera
    '''
    manera_a_ordenar = input("La quiere ordenar de manera ascendente(asc) o de manera descendente(desc)? ")
    lista_heroes_copiada = lista_heroes_desordenada.copy()
    lista_heroes_ordenada = []

    while len(lista_heroes_copiada) > 0:
        if(manera_a_ordenar == "desc"):
            indice_maximo = buscar_maximo(lista_heroes_copiada,"fuerza")
            elemento_maximo = lista_heroes_copiada.pop(indice_maximo)
            lista_heroes_ordenada.append(elemento_maximo)
        elif(manera_a_ordenar == "asc"):
            indice_minimo = buscar_minimo(lista_heroes_copiada,"fuerza")
            elemento_minimo = lista_heroes_copiada.pop(indice_minimo)
            lista_heroes_ordenada.append(elemento_minimo)
        else:
            print("ERROR, no existe el tipo de orden")
            break
    mensaje = ""
    for heroe in lista_heroes_ordenada:
        nombre_heroe = heroe["nombre"]
        fuerza_heroe = heroe["fuerza"]
        mensaje += "Nombre: {0}    Fuerza: {1} \n".format(nombre_heroe, fuerza_heroe)
        
    return mensaje
#-----------------------------------------3-----------------------------------------------------
#print(ordenar_listar_heroes_fuerza(lista_personajes))

def calcular_promedio_key_numerica(lista_heroes:list, key:str, condicion:str)->list:
    '''
    Recibe la lista de personajes, una clave y una condicion (mayor) o (menor)

    Devuelve una lista nueva
    '''
    lista_por_condicion = []
    cantidad_heroes = len(lista_heroes)
    acumulador_key = 0

    for heroe in lista_heroes:

        acumulador_key += heroe[key]
    
    promedio_key = acumulador_key / cantidad_heroes
    print("El promedio es: {0} ".format(promedio_key))

    for heroe in lista_heroes:
        if(condicion == "menor" and heroe[key] < promedio_key):
            lista_por_condicion.append(heroe)
        elif(condicion == "mayor" and heroe[key] > promedio_key):
            lista_por_condicion.append(heroe)

    return lista_por_condicion
#-----------------------------------------4-----------------------------------------------------
#print(calcular_promedio_key_numerica(lista_personajes, "altura", "mayor"))


def buscar_heroes_por_inteligencia(lista_heroes:list, condicion:str)->list:
    '''
    Recibe la lista de personajes y la condicion, (good), (average), (high)

    Devuelve una lista nueva con los personajes con la condicion que el usuario quiera
    '''
    lista_por_inteligencia = []

    for heroe in lista_heroes:
        if(condicion == "good"):
            lista_por_inteligencia.append(heroe)

        elif(condicion == "average"):
            lista_por_inteligencia.append(heroe)
            
        elif(condicion == "high"):
            lista_por_inteligencia.append(heroe)

    return lista_por_inteligencia
#-----------------------------------------5----------------------------------------------------
#print(buscar_heroes_por_inteligencia(lista_personajes,"average"))

# 5- Buscar héroes por inteligencia [good, average, high] y listar en consola los que cumplan dicha búsqueda.










def exportar_csv():
    pass
#-----------------------------------------6---------------------------------------------------
# 6-  Exportar a CSV la lista de héroes ordenada según opción elegida anteriormente [1-4]




