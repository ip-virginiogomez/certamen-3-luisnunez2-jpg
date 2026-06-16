#Problema 3: Sistema de Descuento en Supermercado (20 pts)
#Enunciado: Un supermercado aplica descuentos especiales a sus clientes. Para acceder al descuento, el cliente debe ser mayor de 60 años o tener una tarjeta de socio, y además el total de su compra debe superar los $10.000.

#ndicaciones paso a paso:

#Solicita al usuario su edad, si tiene tarjeta de socio (sí/no) y el monto total de su compra.
#Verifica si cumple las condiciones: el monto debe superar $10.000 y debe ser mayor de 60 años o tener tarjeta de socio.
#Muestra un mensaje indicando si obtiene el descuento del 15% o si no califica, mostrando el monto final en cada caso.
#Puntos asignados: 20 pts

#Criterios evaluados:

#Uso correcto de operadores lógicos (10 pts)
#Validación de condiciones y entrada de datos (5 pts)
#Claridad de la salida (5 pts)
Monto= int(input("Ingrese el Monto a pagar: "))
Edad = int(input("Ingresa la edad del cliente: "))
Tarjeta =(input("Tienes Tarjeta de Socio?: "))

if Monto >= 10000 and (Edad >=60 or Tarjeta == "si"):
    print("Tines un Descuento")
else:
    print(f"No tienes Descuento monto a pagar es de {Monto}")

if Monto >= 10000:
    nuevo_monto = Monto * 0.85
    print(f" Tu nuevo monto a pagar es de:{nuevo_monto}")
    
