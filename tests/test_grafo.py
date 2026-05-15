"""
test_grafo.py - Pruebas de la estructura del grafo.
"""
import sys
sys.path.insert(0, 'src')
from grafo import construir_metro_medellin

def test_total_estaciones():
    metro = construir_metro_medellin()
    assert metro.total_estaciones() >= 35
    print(f"OK - Total estaciones: {metro.total_estaciones()}")

def test_conectividad():
    metro = construir_metro_medellin()
    assert metro.verificar_conectividad()
    print("OK - Red conectada")

def test_transbordos():
    metro = construir_metro_medellin()
    for t in ["San Antonio","Acevedo","Industriales","San Javier"]:
        assert metro.es_transbordo(t)
    print("OK - Transbordos correctos")

def test_cierre_estacion():
    metro = construir_metro_medellin()
    vecinos = metro.cerrar_estacion("Estadio")
    assert not metro.existe("Estadio")
    metro.restaurar_estacion("Estadio", vecinos, "B")
    assert metro.existe("Estadio")
    print("OK - Cierre y restauracion correctos")

if __name__ == "__main__":
    test_total_estaciones()
    test_conectividad()
    test_transbordos()
    test_cierre_estacion()
    print("\nTodas las pruebas de grafo pasaron.")
