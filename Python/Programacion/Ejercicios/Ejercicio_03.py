"""
La división de alimentos de industrias Wayne está trabajando en un pequeño software para cargar datos de heroínas 
y héroes, para para tener un control de las condiciones de heroes existentes, nos solicitan:
1-Nombre de Heroína/Héroe
2-EDAD (mayores a 18 años)
3-Sexo ("m", "f" o "nb")
4-Habilidad ("fuerza", "magia", "inteligencia").
A su vez, el programa deberá mostrar por consola lo siguiente:
A-Dar el nombre de Héroe | Heroína de 'fuerza' más joven.
B-El sexo y nombre de Heroe | Heroína de mayor edad.
C-La cantidad de Heroinas que tienen habilidades de 'fuerza' o 'magia'.
D-El promedio de edad entre Heroinas.
E-El promedio de edad entre Heroes de fuerza.
"""
continuar = "si"
edad_fuerza_mas_joven = 10000000000
flag_edad_fuerza_mas_joven = True
mayor_edad = 0
flag_mayor_edad = True
cantidad_heroinas_fuerza_magia = 0

promedio_edad_heroinas = 0
acumulador_edad_heroinas = 0
cantidad_heroinas = 0

promedio_edad_heroes_fuerza = 0
acumulador_edad_heroes_fuerza = 0
cantidad_heroes_fuerza = 0

while (continuar == "si"):
    nombre = input("Ingrese el nombre del heroe o heroina: ")

    edad = input("Ingrese la edad [+18]: ")
    edad = int(edad)
    while (edad < 18):
        edad = input("ERROR, reingrese la edad [+18]: ")
        edad = int(edad)

    sexo = input("Ingrese el sexo [m], [f], [nb]: ")
    while (sexo != "m" and sexo != "f" and sexo != "nb"):
         sexo = input("ERROR, reingrese el sexo [m], [f], [nb]: ")

    habilidad = input("Ingrese la habilidad [fuerza], [magia], [inteligencia]: ")
    while (habilidad != "fuerza" and habilidad != "magia" and habilidad != "inteligencia"):
        habilidad = input("ERROR, reingrese la habilidad [fuerza], [magia], [inteligencia]: ")
    
    if(edad > mayor_edad or flag_mayor_edad == True):
        mayor_edad = edad
        nombre_mayor_edad = nombre
        sexo_mayor_edad = sexo
        flag_mayor_edad = False

    if (habilidad == "fuerza"):
        if (edad < edad_fuerza_mas_joven or flag_edad_fuerza_mas_joven == True):
            edad_fuerza_mas_joven = edad
            nombre_fuerza_mas_joven = nombre
            flag_edad_fuerza_mas_joven = False
        if (sexo == "m"):
            acumulador_edad_heroes_fuerza = edad
            cantidad_heroes_fuerza += 1

    if (sexo == "f"):
        if (habilidad == "fuerza" or habilidad == "magia"):
            cantidad_heroinas_fuerza_magia += 1
    
    if (sexo == "f"):
        acumulador_edad_heroinas = acumulador_edad_heroinas + edad
        cantidad_heroinas += 1
        
    continuar = input("[si] para continuar [OTRA TECLA] para terminar")

promedio_edad_heroinas = acumulador_edad_heroinas / cantidad_heroinas
promedio_edad_heroes_fuerza = acumulador_edad_heroes_fuerza / cantidad_heroes_fuerza

cantidad_heroinas_fuerza_magia = str(cantidad_heroinas_fuerza_magia)
promedio_edad_heroes_fuerza = str(promedio_edad_heroes_fuerza)
promedio_edad_heroinas = str(promedio_edad_heroinas)

print(" El nombre de Héroe o Heroína de [fuerza] más joven: " + nombre_fuerza_mas_joven)
print("El sexo del heroe o heroina de mayor edad es: " + sexo_mayor_edad + " Y su nombre es: " + nombre_mayor_edad)
print("La cantidad de Heroinas que tienen habilidades de [fuerza] o [magia] es: " + cantidad_heroinas_fuerza_magia)
print("El promedio de edad entre Heroinas es: " + promedio_edad_heroinas)
print("El promedio de edad entre Heroes de fuerza " + promedio_edad_heroes_fuerza)
