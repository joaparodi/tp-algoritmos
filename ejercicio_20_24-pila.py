

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


from stack import Stack


pila = Stack()

personajes = [
    ("Iron Man", 10),
    ("Capitán América", 5),
    ("Thor", 8),
    ("Hulk", 7),
    ("Viuda Negra", 7),
    ("Ojo de Halcón", 6),
    ("Doctor Strange", 4),
    ("Groot", 5),
    ("Rocket Raccoon", 6),
    ("Gamora", 4),
    ("Drax", 4),
    ("Capitana Marvel", 3),
    ("Wanda", 6),
    ("Visión", 4),
    ("Ant-Man", 4),
]

for nombre, peliculas in personajes:
    pila.push((nombre, peliculas))

print()
pila.show()
print()

# a. Posicion de Rocket Raccoon y Groot
print("a. Posición de Rocket Raccoon y Groot:")
pila_aux = Stack()
posicion = 1

while pila.size() > 0:
    nombre, peliculas = pila.pop()
    if nombre == "Rocket Raccoon":
        print(f"   Rocket Raccoon está en la posición {posicion}")
    if nombre == "Groot":
        print(f"   Groot está en la posición {posicion}")
    posicion += 1
    pila_aux.push((nombre, peliculas))

while pila_aux.size() > 0:
    pila.push(pila_aux.pop())

print()

# b. Personajes con más de 5 películas
print("b. Personajes con más de 5 películas:")
pila_aux = Stack()

while pila.size() > 0:
    nombre, peliculas = pila.pop()
    if peliculas > 5:
        print(f"   {nombre} - {peliculas} películas")
    pila_aux.push((nombre, peliculas))

while pila_aux.size() > 0:
    pila.push(pila_aux.pop())

print()

# c. Películas de Viuda Negra
print("c. Películas de Viuda Negra:")
pila_aux = Stack()

while pila.size() > 0:
    nombre, peliculas = pila.pop()
    if nombre == "Viuda Negra":
        print(f"   Viuda Negra participó en {peliculas} películas")
    pila_aux.push((nombre, peliculas))

while pila_aux.size() > 0:
    pila.push(pila_aux.pop())

print()

# d. Personajes que empiezan con C, D o G
print("d. Personajes que empiezan con C, D o G:")
pila_aux = Stack()

while pila.size() > 0:
    nombre, peliculas = pila.pop()
    if nombre[0] in ("C", "D", "G"):
        print(f"   {nombre}")
    pila_aux.push((nombre, peliculas))

while pila_aux.size() > 0:
    pila.push(pila_aux.pop())
    
    
    