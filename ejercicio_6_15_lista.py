

from random import randint
from list_ import List
from pokemones import Pokemons
from entrenadores import Entrenadores


# TP 4 - Lista

# resolver los ejercicios 6 y 15 de lista del libro



# -------5. Dada una lista de números enteros eliminar de estas los números primos---------

# lista = List()

# def cargar(lista: List):
#     for i in range(10):
#         lista.append(randint(0,20))


# cargar(lista)
# print("lista original :")
# lista.show()
# print()

# def es_primo(num):
#     if num < 2:
#         return False
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             return False
#     return True

# def elimi_primo(lista: List):
#     primos = List()
    
#     for i in range(lista.size()):
#         numero = lista[i]
#         if es_primo(numero):
#             primos.append(numero)
            
#     for i in range(primos.size()):
#         lista.delete_value(primos[i])
    
            
# elimi_primo(lista)
# print()
# print("lista sin los numeros primos :")
# lista.show()



# 15. Se cuenta con una lista de entrenadores Pokémon. De cada uno de estos se conoce: nombre, can-
# tidad de torneos ganados, cantidad de batallas perdidas y cantidad de batallas ganadas. Y ade-
# más la lista de sus Pokémons, de los cuales se sabe: nombre, nivel, tipo y subtipo. Se pide resolver

# las siguientes actividades utilizando lista de lista implementando las funciones necesarias:
# a. obtener la cantidad de Pokémons de un determinado entrenador;
# b. listar los entrenadores que hayan ganado más de tres torneos;
# c. el Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados;
# d. mostrar todos los datos de un entrenador y sus Pokémos;
# e. mostrar los entrenadores cuyo porcentaje de batallas ganados sea mayor al 79 %;
# f. los entrenadores que tengan Pokémons de tipo fuego y planta o agua/volador
# (tipo y subtipo);
# g. el promedio de nivel de los Pokémons de un determinado entrenador;
# h. determinar cuántos entrenadores tienen a un determinado Pokémon;
# i. mostrar los entrenadores que tienen Pokémons repetidos;

# j. determinar los entrenadores que tengan uno de los siguientes Pokémons: Tyrantrum, Te-
# rrakion o Wingull;

# k. determinar si un entrenador “X” tiene al Pokémon “Y”, tanto el nombre del entrenador
# como del Pokémon deben ser ingresados; además si el entrenador tiene al Pokémon se
# deberán mostrar los datos de ambos;


class Entrenador:
    def __init__(self, nombre, torneos_ganados, batallas_perdidas, batallas_ganadas,lista_p: List):
        self.nombre = nombre
        self.torneos_ganados = torneos_ganados
        self.batallas_perdidas = batallas_perdidas
        self.batallas_ganadas = batallas_ganadas
        self.pokemons = lista_p # Lista de Pokémons
    
    def __str__(self):
        return (f"Nombre: {self.nombre}, Torneos Ganados: {self.torneos_ganados}, Batallas Perdidas: {self.batallas_perdidas}, Batallas Ganadas: {self.batallas_ganadas}")

class Pokemon:
    def __init__(self, nombre, nivel, tipo, subtipo):
        self.nombre = nombre
        self.nivel = nivel
        self.tipo = tipo
        self.subtipo = subtipo
    
    def __str__(self):
        return (f"Nombre: {self.nombre}, Nivel: {self.nivel}, Tipo: {self.tipo}, Subtipo: {self.subtipo}")


lista_p = List()
lista = List()

def cargar_entrenadores(lista: List):
    for entrenador in Entrenadores:
        lista.append(Entrenador(entrenador["nombre"], entrenador["torneos_ganados"], entrenador["batallas_perdidas"], entrenador["batallas_ganadas"], [Pokemon(pokemon["nombre"], pokemon["nivel"], pokemon["tipo"], pokemon["subtipo"]) for pokemon in entrenador["pokemons"]]))

def cargar_pokemones(lista_p: List):
    for pokemon in Pokemons:
        lista_p.append(Pokemon(pokemon["nombre"], pokemon["nivel"], pokemon["tipo"], pokemon["subtipo"]))

cargar_entrenadores(lista)
cargar_pokemones(lista_p)
lista.show()



