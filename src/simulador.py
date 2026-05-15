"""
simulador.py - Menu principal del simulador del Metro de Medellin.
"""
from grafo import construir_metro_medellin
from dijkstra import dijkstra, imprimir_ruta_rapida
from bfs import bfs_menos_transbordos, imprimir_ruta_transbordos

def mostrar_estaciones(metro):
    print("\n=== ESTACIONES POR LINEA ===")
    for linea, estaciones in metro.lineas.items():
        print(f"Linea {linea}: {' - '.join(estaciones)}")

def comparar_rutas(metro, origen, destino):
    print(f"\n{'='*50}")
    print(f"COMPARACION: {origen} -> {destino}")
    print(f"{'='*50}")
    tiempo, ruta_r, transbordos_r = dijkstra(metro, origen, destino)
    num_t, ruta_t, transbordos_t = bfs_menos_transbordos(metro, origen, destino)
    if tiempo is None:
        print("No hay ruta disponible.")
        return
    print(f"\n[Ruta mas rapida]")
    print(f"  Tiempo: {tiempo} min | Paradas: {len(ruta_r)-1} | Transbordos: {len(transbordos_r)}")
    print(f"  Ruta: {' -> '.join(ruta_r)}")
    print(f"\n[Ruta menos transbordos]")
    print(f"  Transbordos: {num_t} | Paradas: {len(ruta_t)-1}")
    print(f"  Ruta: {' -> '.join(ruta_t)}")

def simular_cierre(metro, estacion_cerrada, origen, destino):
    print(f"\n=== CIERRE: {estacion_cerrada} ===")
    tiempo_orig, ruta_orig, _ = dijkstra(metro, origen, destino)
    print(f"Ruta original: {' -> '.join(ruta_orig)} ({tiempo_orig} min)")
    linea_original = None
    for linea, estaciones in metro.lineas.items():
        if estacion_cerrada in estaciones:
            linea_original = linea
            break
    vecinos = metro.cerrar_estacion(estacion_cerrada)
    print(f"Estacion '{estacion_cerrada}' CERRADA.")
    if not metro.verificar_conectividad():
        print("ADVERTENCIA: La red quedo desconectada.")
    tiempo_alt, ruta_alt, _ = dijkstra(metro, origen, destino)
    if tiempo_alt is None:
        print(f"No hay ruta alternativa entre {origen} y {destino}.")
    else:
        print(f"Ruta alternativa: {' -> '.join(ruta_alt)} ({tiempo_alt} min)")
        print(f"Tiempo adicional: +{tiempo_alt - tiempo_orig} min")
    if linea_original:
        metro.restaurar_estacion(estacion_cerrada, vecinos, linea_original)
    print(f"Estacion '{estacion_cerrada}' restaurada.")

def menu():
    metro = construir_metro_medellin()
    print("\n*** SIMULADOR METRO DE MEDELLIN ***")
    print(metro)
    while True:
        print("\n--- MENU ---")
        print("1. Ver estaciones por linea")
        print("2. Ruta mas rapida (Dijkstra)")
        print("3. Ruta menos transbordos (BFS)")
        print("4. Comparar ambas rutas")
        print("5. Simular cierre de estacion")
        print("6. Estaciones hub")
        print("7. Verificar conectividad")
        print("0. Salir")
        opcion = input("\nElige una opcion: ").strip()
        if opcion == "1":
            mostrar_estaciones(metro)
        elif opcion == "2":
            origen = input("Estacion origen: ").strip()
            destino = input("Estacion destino: ").strip()
            imprimir_ruta_rapida(metro, origen, destino)
        elif opcion == "3":
            origen = input("Estacion origen: ").strip()
            destino = input("Estacion destino: ").strip()
            imprimir_ruta_transbordos(metro, origen, destino)
        elif opcion == "4":
            origen = input("Estacion origen: ").strip()
            destino = input("Estacion destino: ").strip()
            comparar_rutas(metro, origen, destino)
        elif opcion == "5":
            estacion = input("Estacion a cerrar: ").strip()
            origen = input("Estacion origen: ").strip()
            destino = input("Estacion destino: ").strip()
            simular_cierre(metro, estacion, origen, destino)
        elif opcion == "6":
            print("\n=== ESTACIONES HUB ===")
            for estacion, grado in metro.estaciones_hub()[:10]:
                marca = " <-- TRANSBORDO" if metro.es_transbordo(estacion) else ""
                print(f"  {estacion}: {grado} conexiones{marca}")
        elif opcion == "7":
            conectado = metro.verificar_conectividad()
            print(f"\nRed conectada: {'Si' if conectado else 'NO'}")
        elif opcion == "0":
            print("Hasta luego.")
            break
        else:
            print("Opcion no valida.")

if __name__ == "__main__":
    menu()
