
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

for i in notificacion:
    cola.arrive(i)

#cola.show()

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


def contar_rango_horas(cola):
    inicio = '11:43'
    fin = '15:57'

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

    return contador



print('Cola original:')
cola.show()

print('Notificaciones de Twitter con Python:')
mostrar_twitter_python(cola)

contador = contar_rango_horas(cola)
print(f"Notificaciones entre 11:43 y 15:57: {contador}")
