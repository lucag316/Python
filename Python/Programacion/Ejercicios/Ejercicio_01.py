""""
La división de higiene está trabajando en un control de stock para productos sanitarios. Debemos realizar la carga de 5 (cinco) productos de prevención de contagio, de cada una debe obtener los siguientes datos:
1-El tipo (validar "barbijo", "jabón" o "alcohol")
2-El precio: (validar entre 100 y 300)
3-La cantidad de unidades ( no puede ser 0 ni negativo y no debe superar las 1000 unidades)
4-La marca y el Fabricante.
  
 Se debe informar lo siguiente:
A-Del más caro de los barbijos, la cantidad de unidades y el fabricante.
B-Del ítem con más unidades, el fabricante.
C-Cuántas unidades de jabones hay en total.
"""
barbijo_mas_caro = 0
flag_barbijo = True
mayor_cantidad_de_unidades = 0
flag_unidades = True
cantidad_jabones = 0

for producto in range(5):
    tipo = input("Ingrese el tipo: (barbijo), (jabon) o (alcohol)")
    while (tipo != "barbijo" and tipo != "jabon" and tipo != "alcohol"):
        tipo = input("ERROR, reingrese el tipo: (barbijo), (jabon) o (alcohol)")

    precio = input("Ingrese el precio")
    precio = int(precio)
    while(precio < 100 or precio > 300):
        precio = input("ERROR,reingrese el precio")

    cantidad_de_unidades = input("Ingrese la cantidad de unidades")
    cantidad_de_unidades = int(cantidad_de_unidades)
    while(cantidad_de_unidades < 1 or cantidad_de_unidades > 1000):
        cantidad_de_unidades = input("ERROR, reingrese la cantidad de unidades")

    marca = input("Ingrese la marca")
    fabricante = input("Ingrese el fabricante")

    if(tipo == "barbijo"):
        if(precio == barbijo_mas_caro or flag_barbijo == True):
            barbijo_mas_caro = precio
            barbijo_mas_caro_unidades = cantidad_de_unidades
            barbijo_mas_caro_fabricante = fabricante
            flag_barbijo = False
    """
    if (tipo == "barbijo" and flag_barbijo == True):
        barbijo_mas_caro = precio
        flag_barbijo = False
    elif(tipo == "barbijo" and precio > barbijo_mas_caro):
        barbijo_mas_caro = precio
    """
    if(cantidad_de_unidades < mayor_cantidad_de_unidades or flag_unidades == True):
        mayor_cantidad_de_unidades = cantidad_de_unidades
        fabricante_mayor_unidades = fabricante
        flag_unidades = False
    
    if(tipo == "jabon"):
        cantidad_jabones += 1

print("La cantidad de unidades del barbijo mas caro es: " + mayor_cantidad_de_unidades + 
" y el fabricante es: " + barbijo_mas_caro_fabricante)
print("El fabricante del item con mas unidades es: " + fabricante_mayor_unidades)
print("Unidades de jabones: " + cantidad_jabones)
