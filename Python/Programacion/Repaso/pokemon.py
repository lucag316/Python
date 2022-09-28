from Pokemon_info import pokemones
# Nivel 1 - [En clase de repaso]
# 01 - Imprimir nombres de pokemones
# 02 - Imprimir pokemones que tenga un ID par
# 03 - Imprimir pokemones que tenga un ID múltiplo de 25
# 04 - Imprimir nombre de pokemones con su ID de prefijo.
# 05 - Imprimir los pokemones con más poder y cuánto poder tienen (misma fuerza)
# 06 - Imprimir los pokemones con menos poder y cuánto poder tienen (misma fuerza)
"""
            "id": 1,
            "nombre": "bulbasaur",
            "tipo": ["planta"],
            "evoluciones": ["ivysaur", "venusaur"],
            "poder": 4,
            "fortaleza":["agua"],
            "debilidad":["fuego"]
"""
def nombrar_pokemones(): #01
    for personaje in pokemones:
        print(personaje["nombre"])

def calcular_id_par(): #02
    for personaje in pokemones:
        
        if(int(personaje["id"]) % 2 == 0):
            print(personaje)

def calcular_id_multiplo_25(): #03 faltaaaaaaaa
    for personaje in pokemones:

        if(int(personaje["id"]) ):
            pass
#04 faltaaaaaaaaa
