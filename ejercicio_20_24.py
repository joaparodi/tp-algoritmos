

#actividades del tp: pila

#20. Realizar un algoritmo que registre los movimientos de un robot, los datos que se guardan son
#cantidad de pasos y dirección –suponga que el robot solo puede moverse en ocho direcciones:
#norte, sur, este, oeste, noreste, noroeste, sureste y suroeste–. Luego desarrolle otro algoritmo
#que genere la secuencia de movimientos necesarios para hacer volver al robot a su lugar de
#partida, retornando por el mismo camino que fue.

from random import randint
from stack import Stack


pila = Stack()
movimientos = ["norte", "sur", "este", "oeste", "noreste", "noroeste", "sureste", "suroeste"]

print("Movimientos del robot:")
input("Presione Enter para generar movimientos aleatorios...")

for i in range(10):
    pasos = randint(1, 5)
    direccion = movimientos[randint(0, len(movimientos) - 1)]
    pila.push(f"{pasos} pasos hacia {direccion}")

print()
pila.show()

pila_aux = Stack()

while pila.size() > 0:
    pila_aux.push(pila.pop())

pila = pila_aux

print("\nSecuencia de regreso:")
pila.show()


#Dada una pila de personajes de Marvel Cinematic Universe (MCU), de los cuales se dispone de
#su nombre y la cantidad de películas de la saga en la que participó, implementar las funciones
#necesarias para resolver las siguientes actividades:

#a. determinar en qué posición se encuentran Rocket Raccoon y Groot, tomando como posi-
#ción uno la cima de la pila;

#[86]

#b. determinar los personajes que participaron en más de 5 películas de la saga, además indi-
#car la cantidad de películas en la que aparece;

#c. determinar en cuantas películas participo la Viuda Negra (Black Widow);
#d. mostrar todos los personajes cuyos nombre empiezan con C, D y G.
