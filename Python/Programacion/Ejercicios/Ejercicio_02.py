"""
La división de alimentos está trabajando en un pequeño software para cargar las compras
de ingredientes para la cocina de Industrias Wayne. 
Realizar el algoritmo permita ingresar los datos de una compra de ingredientes para
preparar comida al por mayor, HASTA QUE EL CLIENTE QUIERA.
1-PESO: (entre 10 y 100 kilos)
2-PRECIO POR KILO: (mayor a 0 [cero]).
3-TIPO VALIDAD: ("v", "a", "m");(vegetal, animal, mezcla).
Además tener en cuenta que si compro más de 100 kilos en total tenes 15% de descuento sobre el precio bruto.
o si compro más de 300 kilos en total, tenes 25% de descuento sobre el precio bruto.
A-El importe total a pagar, BRUTO sin descuento.
B-El importe total a pagar con descuento (Solo si corresponde).
C-Informar el tipo de alimento más caro.
D-El promedio de precio por kilo en total.
"""

continuar = "si"
precio = 0
acumulador_kilos = 0
acumulador_precios = 0
acumulador_precio_descuento = 0
alimento_mas_caro = 0
flag_alimento_mas_caro = True

while (continuar == "si"):
    peso = input("Igrese el peso, (entre 10 y 100 kilos): ")
    peso = int(peso)
    while (peso < 10 or peso > 100):
        peso = input("ERROR, reingrese el peso, (entre 10 y 100 kilos): ")
        peso = int(peso)
    
    precio_kilo = input("Ingrese el precio por kilo: ")
    precio_kilo = int(precio_kilo)
    while (precio_kilo < 0):
        precio_kilo = input("ERROR, reingrese el precio por kilo: ")
        precio_kilo = int(precio_kilo)


    tipo = input("Ingrese el tipo [v], [a], [m]  (vegetal, animal, mezcla) ")
    while (tipo != "v" and tipo != "a" and tipo != "m"):
        tipo = input("ERROR, reingrese el tipo [v], [a], [m]  (vegetal, animal, mezcla) ")

    acumulador_kilos = acumulador_kilos + peso
    acumulador_precios = acumulador_precios + precio_kilo
    acumulador_precio_descuento = acumulador_precio_descuento + precio_kilo

    if (precio_kilo > alimento_mas_caro or flag_alimento_mas_caro == True):
        alimento_mas_caro = precio_kilo
        tipo_alimento_mas_caro = tipo
        flag_alimento_mas_caro = False

    continuar = input("[si] para continuar [OTRA TECLA] para terminar ")

if (acumulador_kilos > 99 and  acumulador_kilos < 300):
    acumulador_precio_descuento = acumulador_precio_descuento * 0.85

if(acumulador_kilos > 299):
    acumulador_precio_descuento = acumulador_precio_descuento * 0.75

promedio_precio_kilo = acumulador_precios / acumulador_kilos

acumulador_precio_descuento = str(acumulador_precio_descuento)
acumulador_precios = str(acumulador_precios)
promedio_precio_kilo = str(promedio_precio_kilo)

print("El importe total en bruto a pagar es: " + acumulador_precios)
print("El importe a pagar con descuento es: " + acumulador_precio_descuento)
print("El alimento mas caro es: " + tipo_alimento_mas_caro)
print("El promedio de precio por kilo en total es: " + promedio_precio_kilo)
