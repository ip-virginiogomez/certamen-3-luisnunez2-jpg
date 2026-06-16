#Problema 2: Registro de Ventas de una Tienda (35 pts)
#Enunciado: Una pequeña tienda registra las ventas diarias de 3 vendedores durante 3 días de la semana. El dueño quiere saber el rendimiento de cada vendedor y si alguno tuvo bajo desempeño.

#Indicaciones paso a paso:

#Crea una matriz 3x3 para guardar los montos de ventas (cada fila es un vendedor, cada columna es un día).
#Calcula el total de ventas de cada vendedor (suma por fila solamente).
#Identifica qué vendedor tuvo el mayor total de ventas.
#Muestra una alerta si el total de algún vendedor es menor a $30.000.
#Puntos asignados: 35 pts

#Criterios evaluados:

#Representación correcta de la matriz (10 pts)
#Cálculo correcto del total por vendedor (10 pts)
#Identificación del mejor vendedor (10 pts)
#Claridad en mensajes y formato (5 pts)

Ventas = [
    [30000,50000,10000],
    [20000,10000,75000],
    [55000,15000,20000]
]
for fila in Ventas:
    suma = sum(Ventas)


    Venta_Maxima = max(Ventas)
    print(f"el Vendedor {i+1} fue el con ventas mas altas con unas ventas de {Venta_Maxima}")
    #lo di todo 
