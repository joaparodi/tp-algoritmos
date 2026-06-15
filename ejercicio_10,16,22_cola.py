
from stack import Stack
from queue import  Queue




#Debera resolver los ejercicios 10, 16 (no resolver aun dejar pendiente) y 22

#10. Dada una cola con las notificaciones de las aplicaciones de redes sociales de un Smartphone,
#de las cual se cuenta con la hora de la notificación, la aplicación que la emitió y el mensaje,
#resolver las siguientes actividades:

#a. escribir una función que elimine de la cola todas las notificaciones de Facebook;
#b. escribir una función que muestre todas las notificaciones de Twitter, cuyo mensaje incluya
#la palabra ‘Python’, si perder datos en la cola;
#c. utilizar una pila para almacenar temporáneamente las notificaciones producidas entre las
#11:43 y las 15:57, y determinar cuántas son.

cola = Queue()

notificacion =( 
    {'hora': '10:00', 'app': 'Facebook', 'mensaje': 'Tienes una nueva solicitud'},
    {'hora': '12:30', 'app': 'Twitter', 'mensaje': 'Qué bueno es programar en Python!'},
    {'hora': '15:00', 'app': 'Instagram', 'mensaje': 'A @usuario le gustó tu foto'},
    {'hora': '16:00', 'app': 'Twitter', 'mensaje': 'Día de descanso'})

def cargarnot_app(cola:Queue):
    for i in notificacion:
        cola.arrive(i)
# cargarnot_app(cola)
# cola.show()

def eliminar_facebook(cola):
    aux = Queue()
    while cola.size() > 0:
        notificacion = cola.attention()
        if notificacion['app'] != 'Facebook':
            aux.arrive(notificacion)

    while aux.size() > 0:
        cola.arrive(aux.attention())


def mostrar_twitter_python(cola):
    aux = Queue()
    while cola.size() > 0:
        notificacion = cola.attention()
        app = notificacion['app']
        mensaje = notificacion['mensaje']
        if app == 'Twitter' and 'python' in mensaje.lower():
            print(notificacion)
        aux.arrive(notificacion)

    while aux.size() > 0:
        cola.arrive(aux.attention())


def procesar_rango_horas(cola):
    inicio = '11:43'
    fin = '15:57'

    hora_inicio = int(inicio[0:2])
    minuto_inicio = int(inicio[3:5])
    hora_fin = int(fin[0:2])
    minuto_fin = int(fin[3:5])

    horas_totales = hora_fin - hora_inicio
    minutos_totales = minuto_fin - minuto_inicio

    aux = Queue()
    pila = Stack()
    contador = 0

    while cola.size() > 0:
        notificacion = cola.attention()
        hora = notificacion['hora']

        if inicio <= hora <= fin:
            pila.push(notificacion)
            contador += 1

        aux.arrive(notificacion)

    while aux.size() > 0:
        cola.arrive(aux.attention())

    return contador, pila, horas_totales, minutos_totales


# print('COLA ORIGINAL')
# cola.show()

# print('Eliminando Facebook')
# eliminar_facebook(cola)

# print('Twitter + Python')
# mostrar_twitter_python(cola)

# print('Rango de horas y pila temporal')
# cant_notificaciones, pila_notificaciones, hs, mins = procesar_rango_horas(cola)
# print(f"Cantidad de notificaciones entre 11:43 y 15:57: {cant_notificaciones}")
# print(f"Intervalo de tiempo: {hs} horas y {mins} minutos")
# print('Notificaciones almacenadas temporalmente en la pila:')
# pila_notificaciones.show()

# print('COLA FINAL')
# cola.show()



# 22. Se tienen una cola con personajes de Marvel Cinematic Universe (MCU), de los cuales se cono-
# ce el nombre del personaje, el nombre del superhéroe y su género (Masculino M y Femenino

# F) –por ejemplo {Tony Stark, Iron Man, M}, {Steve Rogers, Capitán América, M}, {Natasha Ro-
# manoff, Black Widow, F}, etc., desarrollar un algoritmo que resuelva las siguientes actividades:

# a. determinar el nombre del personaje de la superhéroe Capitana Marvel;
# b. mostrar los nombre de los superhéroes femeninos;
# c. mostrar los nombres de los personajes masculinos;
# d. determinar el nombre del superhéroe del personaje Scott Lang;
# e. mostrar todos datos de los superhéroes o personaje cuyos nombres comienzan con la letra S;
# f. determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre de superhéroes.


cola = Queue()

class personajes:
    
    def __init__(self,nombre,alias,genero):
        self.nombre=nombre
        self.alias=alias
        self.genero=genero
    
    def __str__(self):

        return (f"{self.nombre}--{self.alias}--{self.genero}")    


datos = [
    {"personaje": "Tony Stark", "superheroe": "Iron Man", "genero": "M"},
    {"personaje": "Steve Rogers", "superheroe": "Capitan America", "genero": "M"},
    {"personaje": "Natasha Romanoff", "superheroe": "Black Widow", "genero": "F"},
    {"personaje": "Carol Danvers", "superheroe": "Capitana Marvel", "genero": "F"},  
    {"personaje": "Scott Lang", "superheroe": "Ant-Man", "genero": "M"},
    {"personaje": "Sharon Carter", "superheroe": "Agent 13", "genero": "F"}
 ]
#lista para comprobar en caso de que no halla personajes con s
# datos =[
#     {"personaje": "Natasha Romanoff", "superheroe": "Black Widow", "genero": "F"},
#     {"personaje": "Carol Danvers", "superheroe": "Capitana Marvel", "genero": "F"},
#     {"personaje": "Tony Stark", "superheroe": "Iron Man", "genero": "M"}
#  ]

cola = Queue()

def cargar(cola: Queue ,lista_datos):
    
    for d in lista_datos:
        nuevo_p = personajes(d["personaje"], d["superheroe"], d["genero"])
        cola.arrive(nuevo_p)



cargar(cola,datos)
cola.show()

# a. determinar el nombre del personaje de la superhéroe Capitana Marvel;

def n_capitanamarvel(cola: Queue):
    print("el nombre de la capitana marvel es:")
    
    for i in range(cola.size()):
        buscado = cola.on_front()
        
        if buscado.alias == "Capitana Marvel":
         print(buscado.nombre)
        cola.move_to_end()

n_capitanamarvel(cola)
#cola.show()

# b. mostrar los nombre de los superhéroes femeninos;

def sup_f(cola: Queue):
    print("nombres de los personajes femeninos:")
    for i in range(cola.size()):
        femen = cola.on_front()
        if femen.genero == "F":
            print(femen.nombre)
        cola.move_to_end()

sup_f(cola)
#cola.show()

# c. mostrar los nombres de los personajes masculinos;

def nom_m(cola: Queue):
    print("nombre de personajes masculinos:")
    for i in range(cola.size()):
        mascu = cola.on_front()
        if mascu.genero == "M":
            print(mascu.nombre)
        cola.move_to_end()

nom_m(cola)
#cola.show()


# d. determinar el nombre del superhéroe del personaje Scott Lang;

def n_scott(cola: Queue):
    n_encon = None
    print("el nombre de superheroe de scott lang es:")
    for i in range(cola.size()):
        supscott = cola.on_front()
        if supscott.nombre == "Scott Lang":
            n_encon = supscott.alias
        cola.move_to_end()
    return n_encon

esta_scott = n_scott(cola)

if esta_scott:
    print(esta_scott)
else:
    print("no se encontro scott lang")

# e. mostrar todos datos de los superhéroes o personaje cuyos nombres comienzan con la letra S;

def nom_con_s(cola: Queue):
    lista_encontrados = [] # Iniciamos una lista vacía
    print("datos de los superheroes cuyo nombre empieza con s:")
    for i in range(cola.size()):
        nom_s = cola.on_front()
        if nom_s.nombre[0] == ("S"):
            lista_encontrados.append(nom_s) # Guardamos cada coincidencia
        cola.move_to_end()
        
    return lista_encontrados

resultados = nom_con_s(cola)

if len(resultados) > 0:
    for p in resultados:
        print(p) # Esto llamará automáticamente al __str__ de tu clase
else:
    print("No se encontraron personajes cuyos nombres empiecen con S.")



# f. determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre de superhéroes.

def indi_carol(cola: Queue):
    encontrado = None
    print("verificacion de personaje carol danvers:")
    for i in range(cola.size()):
        nom_bus = cola.on_front()
        if nom_bus.nombre == "Carol Danvers":
            encontrado = nom_bus.alias
        cola.move_to_end()
    return encontrado


resultado = indi_carol(cola)

if resultado:
    print(f"Se encontró a Carol Danvers. Su nombre de superhéroe es: {resultado}")
else:
    print("No se encontró a Carol Danvers en la cola.")


