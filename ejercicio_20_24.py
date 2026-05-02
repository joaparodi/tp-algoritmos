
from random import randint
from queue import Queue

# EJERCICIO 20
#Desarrollar un algoritmo para el control de un puesto de peaje (que posee 3 cabinas de cobro),
#que resuelva las siguientes actividades:
#a. agregar 30 vehículos de manera aleatoria a las cabinas de cobro, los tipos de vehículos son
#los siguientes:
#I. automóviles (tarifa $47);
#II. camionetas (tarifa $59);
#III. camiones (tarifa $71);
#IV. colectivos (tarifa $64).
#b. realizar la atención de las cabinas, considerando las tarifas del punto anterior.
#c. determinar qué cabina recaudó mayor cantidad de pesos ($).
#d. determinar cuántos vehículos de cada tipo se atendieron en cada cola.

#Configuración
VEHICULOS = {
    1: ("automovil",  47),
    2: ("camioneta",  59),
    3: ("camion",     71),
    4: ("colectivo",  64),
}

CANTIDAD_CABINAS  = 3
CANTIDAD_VEHICULOS = 30

#a. Agregar 30 vehículos de manera aleatoria a las 3 cabinas
cabinas = [Queue() for _ in range(CANTIDAD_CABINAS)]

for _ in range(CANTIDAD_VEHICULOS):
    tipo_vehiculo = randint(1, 4)
    cabina_destino = randint(0, 2)
    cabinas[cabina_destino].arrive(tipo_vehiculo)

print("=" * 50)
print("       ESTADO INICIAL DE LAS CABINAS")
print("=" * 50)
for i, cabina in enumerate(cabinas):
    nombres = []
    tamanio = cabina.size()
    for _ in range(tamanio):
        tipo = cabina.move_to_end()
        nombres.append(VEHICULOS[tipo][0])
    print(f"  Cabina {i + 1} ({tamanio} vehículos): {', '.join(nombres)}")

#b. Atención de las cabinas + c. recaudación + d. conteo por tipo
recaudacion   = [0, 0, 0]
conteo        = [
    {1: 0, 2: 0, 3: 0, 4: 0},
    {1: 0, 2: 0, 3: 0, 4: 0},
    {1: 0, 2: 0, 3: 0, 4: 0},
]

print("\n" + "=" * 50)
print("         ATENCIÓN DE LAS CABINAS")
print("=" * 50)

for i, cabina in enumerate(cabinas):
    print(f"\n  ── Cabina {i + 1} ──")
    while cabina.size() > 0:
        tipo   = cabina.attention()
        nombre, tarifa = VEHICULOS[tipo]
        recaudacion[i]    += tarifa
        conteo[i][tipo]   += 1
        print(f"    Atendido: {nombre:<12}  →  ${tarifa}")
    print(f"    Subtotal cabina {i + 1}: ${recaudacion[i]}")

print("\n" + "=" * 50)
print("   CABINA CON MAYOR RECAUDACIÓN")
print("=" * 50)

max_recaudacion = max(recaudacion)
cabina_ganadora = recaudacion.index(max_recaudacion) + 1

for i, monto in enumerate(recaudacion):
    marca = " ★" if monto == max_recaudacion else ""
    print(f"  Cabina {i + 1}: ${monto}{marca}")

print(f"\n  → La cabina {cabina_ganadora} recaudó la mayor cantidad: ${max_recaudacion}")

# Vehículos de cada tipo atendidos en cada cola
print("\n" + "=" * 50)
print("   VEHÍCULOS ATENDIDOS POR TIPO EN CADA CABINA")
print("=" * 50)

for i, conteos in enumerate(conteo):
    print(f"\n  Cabina {i + 1}:")
    for tipo, cantidad in conteos.items():
        nombre = VEHICULOS[tipo][0]
        print(f"    {nombre:<12}: {cantidad}")
