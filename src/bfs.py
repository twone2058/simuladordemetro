"""
bfs.py - Ruta con menos transbordos usando BFS por lineas.
"""
from collections import deque

def bfs_menos_transbordos(grafo, origen, destino):
    if not grafo.existe(origen) or not grafo.existe(destino):
        return None, [], []
    cola = deque()
    cola.append((origen, None, 0, [origen]))
    visitados = {}
    mejor = None
    while cola:
        estacion, linea_actual, transbordos, ruta = cola.popleft()
        estado = (estacion, linea_actual)
        if estado in visitados and visitados[estado] <= transbordos:
            continue
        visitados[estado] = transbordos
        if estacion == destino:
            if mejor is None or transbordos < mejor[0]:
                mejor = (transbordos, ruta)
            continue
        for vecino, (tiempo, linea_vecino) in grafo.vecinos(estacion).items():
            nuevo_transbordo = transbordos
            if linea_actual is not None and linea_vecino != linea_actual:
                nuevo_transbordo += 1
            cola.append((vecino, linea_vecino, nuevo_transbordo, ruta + [vecino]))
    if mejor is None:
        return None, [], []
    num_transbordos, ruta = mejor
    transbordos_estaciones = []
    linea_anterior = None
    for i in range(1, len(ruta)):
        vecinos = grafo.vecinos(ruta[i-1])
        if ruta[i] in vecinos:
            linea_tramo = vecinos[ruta[i]][1]
            if linea_anterior is not None and linea_tramo != linea_anterior:
                transbordos_estaciones.append(ruta[i-1])
            linea_anterior = linea_tramo
    return num_transbordos, ruta, transbordos_estaciones

def imprimir_ruta_transbordos(grafo, origen, destino):
    num_transbordos, ruta, transbordos = bfs_menos_transbordos(grafo, origen, destino)
    if num_transbordos is None:
        print(f"No hay ruta entre {origen} y {destino}")
        return
    print(f"\n=== RUTA CON MENOS TRANSBORDOS ===")
    print(f"Origen:  {origen}")
    print(f"Destino: {destino}")
    print(f"Transbordos: {num_transbordos} | Paradas: {len(ruta)-1}")
    print(f"\nItinerario:")
    for i, e in enumerate(ruta):
        marca = "  <-- TRANSBORDO" if e in transbordos else ""
        print(f"  {i+1}. {e}{marca}")

if __name__ == "__main__":
    from grafo import construir_metro_medellin
    metro = construir_metro_medellin()
    imprimir_ruta_transbordos(metro, "Niquia", "Santo Domingo")
    imprimir_ruta_transbordos(metro, "La Estrella", "Vallejuelos")
