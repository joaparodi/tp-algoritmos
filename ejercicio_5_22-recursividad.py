
#                   ACTIDADES DE ENTREGAS:




#5. Desarrollar una función que permita convertir un número romano en un número decimal.
# x -> 10
# v -> 5
def romano_a_decimal( romano):
    valores = {'i': 1, 'v': 5, 'x': 10, 'l': 50, 'c': 100, 'd': 500, 'm': 1000}
    total = 0
    i = 0
    def convertir(i):
        if i >= len(romano):
            return 0
        if i + 1 < len(romano) and valores[romano[i]] < valores[romano[i + 1]]:
            return valores[romano[i + 1]] - valores[romano[i]] + convertir(i + 2)
        else:
            return valores[romano[i]] + convertir(i + 1)
    return convertir(0)

print(romano_a_decimal("xvi"))




#22. El problema de la mochila Jedi. Suponga que un Jedi (Luke Skywalker, Obi-Wan Kenobi, Rey u
#otro, el que más le guste) está atrapado, pero muy cerca está su mochila que contiene muchos
#objetos. Implementar una función recursiva llamada “usar la fuerza” que le permita al Jedi “con
#ayuda de la fuerza” realizar las siguientes actividades:
#a. sacar los objetos de la mochila de a uno a la vez hasta encontrar un sable de luz o que no
#queden más objetos en la mochila;

#b. determinar si la mochila contiene un sable de luz y cuantos objetos fueron necesarios sa-
#car para encontrarlo;

#c. Utilizar un vector para representar la mochila.

def usar_la_fuerza(mochila, i=0):
    # Caso base: no quedan objetos
    if i >= len(mochila): #len()es la cantidad de elementos del vector
        return False, 0

    # Si encuentra el sable de luz
    if mochila[i] == "sable de luz":
        return True, 1

    # Caso recursivo: sigue buscando
    encontrado, cantidad = usar_la_fuerza(mochila, i + 1)
    return encontrado, cantidad + 1

mochila = ["comida", "mapa", "sable de luz", "ropa"]#anotacion para mi= vector que representa la mochila
print(usar_la_fuerza(mochila))