"""
dijkstra.py - Ruta mas rapida entre dos estaciones usando Dijkstra.
Considera tiempo de recorrido mas costo adicional por transbordo (3 min).
"""
import heapq

COSTO_TRANSBORDO = 3

def dijkstra(grafo, origen, destino):
    if not grafo.existe(origen) or not grafo.existe(destino):
        return None, [], []
    distancias = {e: float('inf') for e in grafo.estaciones}
    distancias[origen] = 0
    anteriores = {e: None for e in grafo.estaciones}
    linea_llegada = {e: None for e in grafo.estaciones}
    heap = [(0, origen, None)]
    while heap:
        tiempo_actual, estacion, linea_actual = heapq.heappop(heap)
        if tiempo_actual > distancias[estacion]:
            continue
        if estacion == destino:
            break
        for vecino, (tiempo, linea) in grafo.vecinos(estacion).items():
            costo_extra = 0
            if linea_actual is not None and linea != linea_actual:
                if grafo.es_transbordo(estacion):
                    costo_extra = COSTO_TRANSBORDO
            nuevo_tiempo = tiempo_actual + tiempo + costo_extra
            if nuevo_tiempo < distancias[vecino]:
                distancias[vecino] = nuevo_tiempo
                anteriores[vecino] = estacion
                linea_llegada[vecino] = linea
                heapq.heappush(heap, (nuevo_tiempo, vecino, linea))
    ruta = []
    actual = destino
    while actual is not None:
        ruta.append(actual)
        actual = anteriores[actual]
    ruta.reverse()
    if ruta[0] != origen:
        return None, [], []
    transbordos = []
    linea_anterior = None
    for i, estacion in enumerate(ruta):
        if i == 0:
            continue
        linea_tramo = linea_llegada[estacion]
        if linea_anterior is not None and linea_tramo != linea_anterior:
            transbordos.append(ruta[i-1])
        linea_anterior = linea_tramo
    return distancias[destino], ruta, transbordos

def imprimir_ruta_rapida(grafo, origen, destino):
    tiempo, ruta, transbordos = dijkstra(grafo, origen, destino)
    if tiempo is None:
        print(f"No hay ruta entre {origen} y {destino}")
        return
    print(f"\n=== RUTA MAS RAPIDA ===")
    print(f"Origen:  {origen}")
    print(f"Destino: {destino}")
    print(f"Tiempo total: {tiempo} minutos")
    print(f"Paradas: {len(ruta)-1} | Transbordos: {len(transbordos)}")
    print(f"\nItinerario:")
    for i, e in enumerate(ruta):
        marca = "  <-- TRANSBORDO" if e in transbordos else ""
        print(f"  {i+1}. {e}{marca}")

if __name__ == "__main__":
    from grafo import construir_metro_medellin
    metro = construir_metro_medellin()
    imprimir_ruta_rapida(metro, "Niquia", "Santo Domingo")
    imprimir_ruta_rapida(metro, "La Estrella", "Vallejuelos")
