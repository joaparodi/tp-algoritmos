
from logging import root
from platform import node
import queue
from typing import Any, Optional

from queue import Queue

class Node():

    def __init__(self, value=None, other_values=None):
        self.value = value
        self.left = None
        self.right = None
        self.other_values = other_values
        self.height = 0
    
    def __str__(self):
        return self.value


class BinaryTree():

    def __init__(self):
        self.root = None

    def height(self, root):
        if root is None:
            return -1
        else:
            return root.height
    
    def update_height(self, root):
        if root is not None:
            left_height = self.height(root.left)
            right_height = self.height(root.right)
            root.height = (left_height if left_height > right_height else right_height) + 1

    def insert_node(self, value: Any, other_value=None) -> None:

        def __insert_node(root, value, other_value=None):
            if root is None:
                # print(f'lugar vacio insertar {value}')
                root = Node(value, other_value)
            elif value < root.value:
                # print(f'ir a la izquierda de {root.value}')
                root.left = __insert_node(root.left, value, other_value)
            else:
                # print(f'ir a la derecha de {root.value}')
                root.right = __insert_node(root.right, value, other_value)
            
            root = self.auto_balance(root)
            self.update_height(root)
            return root
            
        self.root = __insert_node(self.root, value, other_value)

    def delete_node(self, value: Any) -> Optional[Any]:
        def __replace(root):
            # print(root.value)
            aux = None
            if root.right is None:
                # print('mayor encontrado')
                return root.left, root
            else:
                # print('segui buscando a la derecha')
                root.right, aux = __replace(root.right)
            return root, aux

        def __delete_node(root, value):
            x = None
            other_value = None
            if root is not None:
                if value < root.value:
                    # print('ir a la izq')
                    # input()
                    root.left, x, other_value = __delete_node(root.left,value)
                elif value > root.value:
                    # print('ir a la derecha')
                    # input()
                    root.right, x, other_value = __delete_node(root.right, value)
                else:
                    # print('valor encontrado')
                    # input()
                    x = root.value
                    other_value = root.other_values
                    aux = None
                    if root.left is None:
                        # print('no tiene hijo izquierdo')
                        # input()
                        return root.right, x, other_value
                    elif root.right is None:
                        # print('no tiene hijo derecho')
                        # input()
                        return root.left, x, other_value
                    else:
                        # print('buscar remplazo')
                        # input()
                        root.left, aux = __replace(root.left)
                        root.value = aux.value
            return root, x, other_value

        other_value = None
        self.root, x, other_value = __delete_node(self.root, value)

        return x, other_value

    def search(self, value) -> Optional[Any]:
        def __search(root, value):
            aux = None
            if root is not None:
            
                if root.value == value:
                    aux = root
                elif value < root.value:
                    aux = __search(root.left, value)
                elif value > root.value:
                    aux = __search(root.right, value)

            return aux


        node = __search(self.root, value)
        
        return node 
    
    def auto_balance(self, root):
        if root is not None:
            if self.height(root.left) - self.height(root.right) == 2:
                if self.height(root.left.left) >= self.height(root.left.right):
                    root = self.simple_rotation(root, True)
                else:
                    root = self.double_rotation(root, True)
            elif self.height(root.right) - self.height(root.left) == 2:
                if self.height(root.right.right) >= self.height(root.right.left):
                    root = self.simple_rotation(root, False)
                else:
                    root = self.double_rotation(root, False)
        return root

    def simple_rotation(self, root, control):
        if control: # rotaicon hacia la derecha
            aux = root.left
            root.left = aux.right
            aux.right = root
        else: # rotacion hacia la izquierda
            aux = root.right
            root.right = aux.left
            aux.left = root
        
        self.update_height(root)
        self.update_height(aux)
        root = aux
        return root
    
    def double_rotation(self, root, control):
        if control: # rotacion doble a la derecha
            root.left = self.simple_rotation(root.left, False)
            root = self.simple_rotation(root, True)
        else: # rotacion doble izquierda
            root.right = self.simple_rotation(root.right, True)
            root = self.simple_rotation(root, False)
        return root

    def inorden(self) -> None:
        
        def __inorden(root):
            if root is not None:
                if root.left is not None:
                # print(f'anda a la izquierda de {root.value}')
                    __inorden(root.left)
            # print(f'procesa nodo actual')
                print(root.value, root.height)
                if root.right is not None:
                # print(f'anda a a derecha de {root.value}')
                    __inorden(root.right)
            else :
                return None

        __inorden(self.root)
    
    def postorden(self) -> None:
        
        def __postorden(root):
            if root.right is not None:
                __postorden(root.right)
            print(root.value)
            if root.left is not None:
                __postorden(root.left)

        __postorden(self.root)

    def preorden(self) -> None:
        def __preorden(root):
            print(root.value)
            if root.left is not None:
                __preorden(root.left)
            if root.right is not None:
                __preorden(root.right)

        __preorden(self.root)

    def by_level(self) -> None:

        pendings = Queue()

        if self.root is not None:
            pendings.arrive(self.root)
            # print(f'queue')
            # pendings.show()
            # input()
            while pendings.size() > 0:
                node = pendings.attention()
                print(node.value)
                # input()
                if node.left is not None:
                    pendings.arrive(node.left)
                if node.right is not None:
                    pendings.arrive(node.right)
                # print(f'queue ')
                # pendings.show()

                # input()


#funciones usadas en el ejercicio 5

    def inorden_villain(self) -> None:
        
        def __inorden_villain(root):
            if root.left is not None:
                __inorden_villain(root.left)
            if root.other_values['is_villain']:
                print(root.value)
            if root.right is not None:
                __inorden_villain(root.right)

    def postorden_hero(self):
    
        def __postorden_hero(root):
            if root.right is not None:
                __postorden_hero(root.right)
            if not root.other_values['is_villain']:
                print(root.value)
            if root.left is not None:
                __postorden_hero(root.left)

        __postorden_hero(self.root)

    def inorden_hero_star_with(self, prefix: str) -> None:
        
        def __inorden_hero_star_with(root, prefix):
            if root.left is not None:
                __inorden_hero_star_with(root.left, prefix)
            if root.value.startswith(prefix) and not root.other_values['is_villain']:
                print(root.value)
            if root.right is not None:
                __inorden_hero_star_with(root.right, prefix)

        __inorden_hero_star_with(self.root, prefix)

    def proxy_search(self, prefix: str) -> None:
        
        def __proxy_search(root, prefix):
            if root.left is not None:
                __proxy_search(root.left, prefix)
            if prefix in root.value.lower():
                print(f"Encontrado: {root.value} | Datos: {root.other_values}")
                print(root.value)
            if root.right is not None:
                __proxy_search(root.right, prefix)

        __proxy_search(self.root, prefix)

    def count_heroes(self) -> None:
        def __count_heroes(root):
            count = 0
            if root is not None:
                if root.left is not None:
                    count += __count_heroes(root.left)
                if not root.other_values['is_villain']:
                    count += 1
                if root.right is not None:
                    count += __count_heroes(root.right)
            return count

        count = __count_heroes(self.root)
        return count





    def count_villian(self) -> None:
            def __count_villian(root):
                count = 0
                if root is not None:
                    if root.left is not None:
                        count += __count_villian(root.left)
                    if  root.other_values['is_villain']:
                        count += 1
                    if root.right is not None:
                        count += __count_villian(root.right)
                return count
    
            count = __count_villian(self.root)
            return count



    
    def generar_bosque(self):
        """
        Recorre el árbol original y genera un bosque separando 
        a los héroes y villanos en dos árboles independientes.
        """
        arbol_heroes = BinaryTree()
        arbol_villanos = BinaryTree()

        def __recorrer_y_separar(root):
            if root is not None:
                if root.left is not None:
                    __recorrer_y_separar(root.left)
                
                # Usamos tu condición del diccionario
                if root.other_values.get('is_villain'):
                    arbol_villanos.insert_node(root.value, root.other_values)
                else:
                    arbol_heroes.insert_node(root.value, root.other_values)
                    
                if root.right is not None:
                    __recorrer_y_separar(root.right)

        __recorrer_y_separar(self.root)
        
        # Retorna ambos árboles ya armados (el bosque)
        return arbol_heroes, arbol_villanos



    #funciones usadas en el ejercicio 23

    def inorden_criaturas_y_asesinos(self) -> None:
            def __inorden(root):
                if root is not None:
                    __inorden(root.left)
                    # Accedemos directamente a los atributos del objeto Criatura
                    print(f"Criatura: {root.other_values.name} --> Derrotado por: {root.other_values.killer}")
                    __inorden(root.right)
            __inorden(self.root)

    def cargar_des(self) -> None:
        def __cargar(root):
            if root is not None:
                __cargar(root.left)
                print(f"agrega descripcion de :{root.value}")
                res =input("Descripcion:")
                root.other_values.description = res
                __cargar(root.right)  

        __cargar(self.root)


    def derrotadores_criaturas(self) -> list:
        derrotadores = {}

        def contar_derrotadores(root):
            if root is not None:
            # .strip() elimina espacios sobrantes alrededor del texto
                derrotador = root.other_values.killer.strip() if root.other_values.killer else None

                # Filtra que exista, que no sea vacio, ni guion, ni None
                if derrotador and derrotador not in ["-", "", "None", "none"]:
                    if derrotador in derrotadores:
                        derrotadores[derrotador] += 1
                    else:
                        derrotadores[derrotador] = 1

                contar_derrotadores(root.left)
                contar_derrotadores(root.right)

        contar_derrotadores(self.root)

        # Ordena de mayor a menor y toma los primeros 3 del ranking
        top_3_derrotadores = sorted(derrotadores.items(), key=lambda x: x[1], reverse=True)[:3]
        return top_3_derrotadores

    def criaturas_derrotadas_por(self, nombre_heroe) -> list:
        derrotadas = []

        def buscar_killer(root):
            if root is not None:
                if root.other_values.killer == nombre_heroe:
                    derrotadas.append(root.other_values.name)
                buscar_killer(root.left)
                buscar_killer(root.right)

        buscar_killer(self.root)
        return derrotadas
    
    def criaturas_no_derrotadas(self) -> list:
        no_derrotadas = []

        def buscar_no_derrotadas(root):
            if root is not None:
                if root.other_values.killer in ["-", "", "None", "none"]:
                    no_derrotadas.append(root.other_values.name)
                buscar_no_derrotadas(root.left)
                buscar_no_derrotadas(root.right)

        buscar_no_derrotadas(self.root)
        return no_derrotadas


    def mostrar_capturadores(self):
    
        def __mostrar(root):
            if root is not None:
                # 1. Recorrer subárbol izquierdo
                __mostrar(root.left)
            
                # 2. Imprimir el nodo actual y su campo capturada
                capturado = root.other_values.captured if root.other_values and root.other_values.captured else "-"
                print(f"Criatura: {root.value} --> Capturada por: {capturado}")
            
            # 3. Recorrer subárbol derecho
                __mostrar(root.right)

    # Iniciar el recorrido desde la raíz del árbol
        __mostrar(self.root)



    def buscar_por_coincidencia(self, termino_busqueda: str) -> list:
        coincidencias = []
        termino = termino_busqueda.lower().strip()

        def __b_concidencia(root):
            if root is not None:
                # 1. Recorrer el hijo izquierdo si existe
                if root.left is not None:
                    __b_concidencia(root.left)
            
                # 2. Procesar el nodo actual: verificar coincidencia
                if termino in str(root.value).lower():
                    coincidencias.append(root)
            
                # 3. Recorrer el hijo derecho si existe
                if root.right is not None:
                    __b_concidencia(root.right)

        # Iniciar el recorrido desde la raíz del árbol
        __b_concidencia(self.root)
        return coincidencias

    def list_nivel(self) -> list:
        niveles = []
        if self.root is None:
            return niveles

        queue = Queue()
        # Guardamos la tupla (nodo, nivel) y la prioridad 0
        queue.arrive((self.root, 0), 0)

        while queue.size() > 0:
            # attention() devuelve [prioridad, (nodo, nivel)]
            prioridad, (nodo_actual, nivel_actual) = queue.attention()

            while len(niveles) <= nivel_actual:
                niveles.append([])

            niveles[nivel_actual].append(nodo_actual.value)

            # Encolamos los hijos pasando (nodo, nivel + 1) y el nivel como prioridad
            if nodo_actual.left is not None:
                queue.arrive((nodo_actual.left, nivel_actual + 1), nivel_actual + 1)

            if nodo_actual.right is not None:
                queue.arrive((nodo_actual.right, nivel_actual + 1), nivel_actual + 1)

        return niveles
    
    def buscar_criaturas_por_capturador(self, capturador: str = "Heracles") -> list:
        def buscar_capturador(root):
            capturadas = []
            if root is not None:
                if root.left is not None:
                    capturadas += buscar_capturador(root.left)

                if root.other_values.captured == capturador:
                    capturadas.append(root.value)

                if root.right is not None:
                    capturadas += buscar_capturador(root.right)

            return capturadas

        return buscar_capturador(self.root)
    
