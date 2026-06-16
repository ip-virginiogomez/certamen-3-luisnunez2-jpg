#Problema 1: Control de Velocidad en una Autopista (25 pts)
#Enunciado: Una autopista instaló sensores para registrar la velocidad de los vehículos y detectar infracciones. Debes crear un programa que analice los registros y emita alertas cuando corresponda.

#Indicaciones paso a paso:

#Solicita al usuario que ingrese 5 velocidades (en km/h).
#Guarda las velocidades en una lista.
#Calcula el promedio y la velocidad máxima registrada.
#Verifica si todas las velocidades están dentro del límite permitido (entre 60 y 120 km/h).
#Si alguna velocidad supera los 140 km/h o es menor a 20 km/h, muestra una advertencia de peligro.

Velocidades = []
for i in range(5):
    Velocidad = int(input("Ingresa las Velocidades: "))
    Velocidades.append(Velocidad)
    if Velocidad <20:
        print("Advertencia, velociad muy baja")
    elif Velocidad >140:
        print("Velocidad muy alta")

promedio = sum(Velocidades) / len(Velocidades)    
velocidad_Maxima = max(Velocidades)

print(f"El promedio de las Velidades son {promedio}")
print(f"La Velocidad mas alta registrada fue de: {velocidad_Maxima}")
 
