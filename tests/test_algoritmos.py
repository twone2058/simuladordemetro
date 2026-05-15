"""
test_algoritmos.py - Pruebas de Dijkstra y BFS.
"""
import sys
sys.path.insert(0, 'src')
from grafo import construir_metro_medellin
from dijkstra import dijkstra
from bfs import bfs_menos_transbordos

def test_dijkstra_misma_linea():
    metro = construir_metro_medellin()
    tiempo, ruta, _ = dijkstra(metro, "Niquia", "Bello")
    assert tiempo == 2, f"Esperado 2, fue {tiempo}"
    print(f"OK - Dijkstra misma linea: {tiempo} min")

def test_dijkstra_con_transbordo():
    metro = construir_metro_medellin()
    tiempo, ruta, transbordos = dijkstra(metro, "Niquia", "Santo Domingo")
    assert tiempo is not None
    assert len(transbordos) >= 1
    print(f"OK - Dijkstra con transbordo: {tiempo} min, {len(transbordos)} transbordos")

def test_bfs_misma_linea():
    metro = construir_metro_medellin()
    num_t, ruta, _ = bfs_menos_transbordos(metro, "Niquia", "La Estrella")
    assert num_t == 0, f"Esperado 0, fue {num_t}"
    print(f"OK - BFS misma linea: {num_t} transbordos")

def test_estacion_inexistente():
    metro = construir_metro_medellin()
    tiempo, _, _ = dijkstra(metro, "Niquia", "Estacion Falsa")
    assert tiempo is None
    print("OK - Estacion inexistente manejada")

if __name__ == "__main__":
    test_dijkstra_misma_linea()
    test_dijkstra_con_transbordo()
    test_bfs_misma_linea()
    test_estacion_inexistente()
    print("\nTodas las pruebas de algoritmos pasaron.")
