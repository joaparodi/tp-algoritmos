
# TP 5 - Arbol


# Debera resolver los ejercicios 5 y 23 de arbol del libro, subirlos a github y pasar el link en la entrega.

# 5. Dado un árbol con los nombre de los superhéroes y villanos de la saga Marvel Cinematic Universe (MCU), desarrollar un algoritmo que contemple lo siguiente:
# a. además del nombre del superhéroe, en cada nodo del árbol se almacenará un campo booleano que indica si es un héroe o un villano, True y False respectivamente;
# b. listar los villanos ordenados alfabéticamente;
# c. mostrar todos los superhéroes que empiezan con C;
# d. determinar cuántos superhéroes hay el árbol;
# e. Doctor Strange en realidad está mal cargado. Utilice una búsqueda por proximidad para encontrarlo en el árbol y modificar su nombre;
# f. listar los superhéroes ordenados de manera descendente;
# g. generar un bosque a partir de este árbol, un árbol debe contener a los superhéroes y otro a los villanos, luego resolver las siguiente tareas:
#   I. determinar cuántos nodos tiene cada árbol;
#   II. realizar un barrido ordenado alfabéticamente de cada árbol.



from super_heroes_data import superheroes
from criaturas import Criaturas
from tree import BinaryTree


# class MarvelCharacter():

#     def __init__(self, nombre, anio, casa, bio):
#         self.name = nombre
#         self.year = anio
#         self.house = casa
#         self.bio = bio

#     def __str__(self):
#         return f"{self.name} - {self.year} - {self.house}"
    


# arbol_marvel = BinaryTree()

# print(f'cantidad de elementos {len(superheroes)}')
# #A
# for marvel_character in superheroes:
#     arbol_marvel.insert_node(marvel_character['name'], other_value=marvel_character)

# # #B
# print("\n---ejercicio 5.b---")
# # arbol_marvel.inorden_villain()


# # #C
# print("\n---ejercicio 5.c---")
# # arbol_marvel.inorden_hero_star_with('C')

# # #D
# print("\n---ejercicio 5.d---")
# # print(f'cantidad de heroes: {arbol_marvel.count_heroes()}')

# # E
# print("\n---ejercicio 5.e---")
# search_str = input('ingrese lo que quiere buscar(DC.String): ')
# arbol_marvel.proxy_search(search_str.lower())


# search_str = input('ingrese lo que quiere modificar: ')

# node = arbol_marvel.search(search_str)
# if node is not None:
#     new_name = input('ingrese el nuevo nombre: ')
#     delete_value, delete_other_value = arbol_marvel.delete_node(node.value)
#     delete_other_value['name'] = new_name
#     arbol_marvel.insert_node(new_name, delete_other_value)


# arbol_marvel.inorden_hero_star_with('D')


# # F
# print("\n---ejercicio 5.f---")
# arbol_marvel.postorden_hero()

# #G


# arbol_heroes, arbol_villanos = arbol_marvel.generar_bosque()
# print("\n---ejercio 5.g----")
# print("--- I. Cantidad de nodos ---")
# print(f"Nodos en Héroes: {arbol_heroes.count_heroes()}")
# print(f"Nodos en Villanos: {arbol_villanos.count_villian()}")

# # g.II. Realizar un barrido ordenado alfabéticamente de cada árbol
# print("\n---Barrido alfabético de Héroes ---")
# arbol_heroes.inorden()

# print("\n---Barrido alfabético de Villanos ---")
# arbol_villanos.inorden()




# 23.Implementar un algoritmo que permita generar un árbol con los datos de la siguiente tabla y resuelva las siguientes consultas:
# a. listado inorden de las criaturas y quienes la derrotaron;
# b. se debe permitir cargar una breve descripción sobre cada criatura;
# c. mostrar toda la información de la criatura Talos;
# d. determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas;
# e. listar las criaturas derrotadas por Heracles;
# f. listar las criaturas que no han sido derrotadas;
# g. además cada nodo debe tener un campo “capturada” que almacenará el nombre del héroe o dios que la capturo;
# h. modifique los nodos de las criaturas Cerbero, Toro de Creta, Cierva Cerinea y Jabalí de Erimanto indicando que Heracles las atrapó;
# i. se debe permitir búsquedas por coincidencia;
# j. eliminar al Basilisco y a las Sirenas;
# k. modificar el nodo que contiene a las Aves del Estínfalo, agregando que Heracles derroto a varias;
# l. modifique el nombre de la criatura Ladón por Dragón Ladón;
# m. realizar un listado por nivel del árbol;
# n. muestre las criaturas capturadas por Heracles.


class criatura:
    def __init__(self, nombre, asesino, descripcion="", capturada=None):
            self.name = nombre
            self.killer = asesino
            self.description = descripcion
            self.captured = capturada  # Campo solicitado en el punto g
    
    def __str__(self):
        return f"Nombre: {self.name} | Derrotado por: {self.killer} | Capturada por: {self.captured} | Desc: {self.description}"
    
    
arbol_criatura = BinaryTree()

print(len(Criaturas))

def cargar(arbol_criatura : BinaryTree):
    
    for c in Criaturas:
        
        objeto_criatura = criatura(
            nombre=c['name'], 
            asesino=c['killer'], 
            descripcion=c.get('description', ''), 
            capturada=c.get('captured', None)
        )
        
        arbol_criatura.insert_node(c['name'], other_value=objeto_criatura)
        
cargar(arbol_criatura)

arbol_criatura.inorden()

# A
print("\n--listado de criaturas y quienes lo derrotaron")
arbol_criatura.inorden_criaturas_y_asesinos()

# B

# print("\n--cargar descripcion de cada criatura---")

# arbol_criatura.cargar_des()

# C

print("\n--informacion de la criatura de talos---")
talos = arbol_criatura.search("Talos")
if talos is not None:
    print(talos.other_values)
else:
    print(" No se encontró la criatura Talos en el árbol.")


