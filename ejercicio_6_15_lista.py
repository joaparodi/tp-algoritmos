

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



def by_poke_name(item):
    return item.nombre


lista_p = List()
lista = List()

lista_p.add_criterion('nombre', by_poke_name)


def cargar_pokemones(lista_p: List):
    for p in Pokemons:
        lista_p.append(Pokemon(p["nombre"], p["nivel"], p["tipo"], p["subtipo"]))

def cargar_entrenadores(lista: List, lista_p: List):
    for e in Entrenadores:
        pokemons_entrenador = List()
        
        # Buscamos cada Pokémon en lista_p usando la búsqueda binaria de tu clase List
        for nombre_pokemon in e["pokemons"]:
            idx = lista_p.search(nombre_pokemon, 'nombre')
            if idx is not None:
                pokemons_entrenador.append(lista_p[idx])
            
        lista.append(
            Entrenador(
                e["nombre"],
                e["torneos_ganados"],
                e["batallas_perdidas"],
                e["batallas_ganadas"],
                pokemons_entrenador
            )
        )

cargar_pokemones(lista_p)
cargar_entrenadores(lista, lista_p)


lista.show()


# a. obtener la cantidad de Pokémons de un determinado entrenador;
print()
print()

def by_name(item):
    return item.nombre

lista.add_criterion('nombre', by_name)


index=lista.search("Ash",'nombre')

if index is not None:
    entrenador = lista[index]
    print(f"--- Pokémon de {entrenador.nombre} ---")
    
    # Recorremos e imprimimos cada Pokémon de su lista
    for pokemon in entrenador.pokemons:
        print(pokemon)

print()
if index is not None:
    print(f"Cantidad de Pokémons de {lista[index].nombre}: {len(lista[index].pokemons)}")
else:
    print("Entrenador no encontrado")



# b. listar los entrenadores que hayan ganado más de tres torneos;

def entrenadores_mas_de_tres_torneos(lista: List) -> List:
    resultado = List()
    for i in range(lista.size()):
        if lista[i].torneos_ganados > 3:
            resultado.append(lista[i])
    return resultado


ganadores = entrenadores_mas_de_tres_torneos(lista)
ganadores.show() 
print()


# c. el Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados;

def pokemon_mayor_nivel_entrenador(lista: List):
    max_torneos = -1
    entrenador_max = None
    
    for i in range(lista.size()):
        if lista[i].torneos_ganados > max_torneos:
            max_torneos = lista[i].torneos_ganados
            entrenador_max = lista[i]
    
    if entrenador_max is not None:
        max_nivel = -1
        pokemon_max = None
        
        for pokemon in entrenador_max.pokemons:
            if pokemon.nivel > max_nivel:
                max_nivel = pokemon.nivel
                pokemon_max = pokemon
        
        return pokemon_max
    return None



pokemon_mayor = pokemon_mayor_nivel_entrenador(lista)
if pokemon_mayor is not None:   
    print(f"Pokémon de mayor nivel del entrenador con más torneos ganados: {pokemon_mayor}")
else:
    print("No se encontró un entrenador con torneos ganados.")











