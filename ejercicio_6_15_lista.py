

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
# f. los entrenadores que tengan Pokémons de tipo fuego y planta o agua/volador(tipo y subtipo);
# g. el promedio de nivel de los Pokémons de un determinado entrenador;
# h. determinar cuántos entrenadores tienen a un determinado Pokémon;
# i. mostrar los entrenadores que tienen Pokémons repetidos;
# j. determinar los entrenadores que tengan uno de los siguientes Pokémons: Tyrantrum, Terrakion o Wingull;
# k. determinar si un entrenador “X” tiene al Pokémon “Y”, tanto el nombre del entrenador como del Pokémon deben ser ingresados; además si el entrenador tiene al Pokémon se deberán mostrar los datos de ambos;


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

print()
lista.show()


# a. obtener la cantidad de Pokémons de un determinado entrenador;
print()
print()

def by_name(item):
    return item.nombre

lista.add_criterion('nombre', by_name)


index=lista.search("Ash",'nombre')


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


print()
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
        
        return pokemon_max, entrenador_max
    return None



pokemon_mayor , entrenador_max = pokemon_mayor_nivel_entrenador(lista)
if pokemon_mayor is not None:   
    print(f"el entrenador con más torneos ganados es :{entrenador_max.nombre} y el pokemon de mayor nivel que tiene es: {pokemon_mayor}")
else:
    print("No se encontró un entrenador con torneos ganados.")

print()


# d. mostrar todos los datos de un entrenador y sus Pokémos;

nombre = input("Ingrese el nombre del entrenador: ")
pos = lista.search(nombre,'nombre')

if pos is not None:
    entrenador = lista[pos]
    print(f"Datos del entrenador: {entrenador}")
    print("Pokémons:")
    for pokemon in entrenador.pokemons:
        print(pokemon)

print()


# e. mostrar los entrenadores cuyo porcentaje de batallas ganados sea mayor al 79 %;

def entrenadores_porcentaje_batallas(lista: List) -> List:
    resultado = List()
    for i in range(lista.size()):
        total_batallas = lista[i].batallas_ganadas + lista[i].batallas_perdidas
        if total_batallas > 0:
            porcentaje_ganadas = (lista[i].batallas_ganadas / total_batallas) * 100
            if porcentaje_ganadas > 79:
                resultado.append(lista[i])
    return resultado


print()
batallas_ganadas = entrenadores_porcentaje_batallas(lista)
batallas_ganadas.show()



# f. los entrenadores que tengan Pokémons de tipo fuego y planta o agua/volador(tipo y subtipo);
def tipo_pokemon(lista : List) -> List:
    resultado = List()
    for i in range(lista.size()):
        entrenador = lista[i]
        fuego = False
        planta = False
        agua_volador = False
        
        for j in range(entrenador.pokemons.size()):
            p = entrenador.pokemons[j]
            if p.tipo == "Fuego":
                fuego = True
            if p.tipo == "Planta":
                planta = True
            if p.tipo == "Agua" and p.subtipo == "Volador":
                agua_volador = True
        
        # Un solo condicional al final evalúa al entrenador completo
        if (fuego and planta) or agua_volador:
            resultado.append(entrenador)
    
    return resultado

print()
t_pokemon = tipo_pokemon(lista)
t_pokemon.show()



# g. el promedio de nivel de los Pokémons de un determinado entrenador;

def promedio_nivel_entrenador(lista: List, nombre: str) -> float:
    pos = lista.search(nombre, 'nombre')
    if pos is not None:
        entrenador = lista[pos]
        total_nivel = 0
        cantidad_pokemons = entrenador.pokemons.size()
        
        # Recorrido con bucle for usando size() e indexación []
        for j in range(cantidad_pokemons):
            total_nivel += entrenador.pokemons[j].nivel
            
        if cantidad_pokemons > 0:
            return total_nivel / cantidad_pokemons
            
    return 0.0

print()
nombre_entrenador = input("Ingrese el nombre del entrenador: ")
promedio = promedio_nivel_entrenador(lista, nombre_entrenador)
print(f"El promedio de nivel de los Pokémons de {nombre_entrenador} es: {promedio}")
print()

# h. determinar cuántos entrenadores tienen a un determinado Pokémon;


def entrenadores_con_pokemon(lista: List, value: str) -> int:
    cont = 0
    for i in range(lista.size()):
        entrenador = lista[i]
        for j in range(entrenador.pokemons.size()):
            if entrenador.pokemons[j].nombre == value:
                cont += 1
            
    return cont

entrenador_pokemon = input("Ingrese el nombre del Pokémon: ")
cantidad_entrenadores = entrenadores_con_pokemon(lista, entrenador_pokemon)

if cantidad_entrenadores > 0:
    print(f"Cantidad de entrenadores que tienen al Pokémon {entrenador_pokemon}: {cantidad_entrenadores}")
else:
    print(f"Ningún entrenador tiene al Pokémon {entrenador_pokemon}.")
        
print()     

# i. mostrar los entrenadores que tienen Pokémons repetidos;

def entrenadores_con_pokemons_repetidos(lista: List) -> List:
    resultado = List()
    
    for i in range(lista.size()):
        entrenador = lista[i]
        tiene_repetidos = False
        cant_pokemons = entrenador.pokemons.size()
        
        for j in range(cant_pokemons):
            for k in range(j + 1, cant_pokemons):
                if entrenador.pokemons[j].nombre.lower() == entrenador.pokemons[k].nombre.lower():
                    tiene_repetidos = True
                    break 
            if tiene_repetidos:
                break  
        
        if tiene_repetidos:
            resultado.append(entrenador)
            
    return resultado


p_repetidos = entrenadores_con_pokemons_repetidos(lista)
if p_repetidos.size() > 0:
    print("Entrenadores con Pokémons repetidos:")
    p_repetidos.show()
else:
    print("No hay entrenadores con Pokémons repetidos.")



# j. determinar los entrenadores que tengan uno de los siguientes Pokémons: Tyrantrum, Terrakion o Wingull;























