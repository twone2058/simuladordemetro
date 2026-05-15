"""
grafo.py - Modelo del Metro de Medellin como grafo ponderado no dirigido.
Cada estacion es un nodo. Cada tramo es una arista con tiempo en minutos y linea.
"""

class Grafo:
    def __init__(self):
        self.estaciones = {}
        self.lineas = {}
        self.transbordos = set()

    def agregar_estacion(self, nombre, linea):
        if nombre not in self.estaciones:
            self.estaciones[nombre] = {}
        if linea not in self.lineas:
            self.lineas[linea] = []
        if nombre not in self.lineas[linea]:
            self.lineas[linea].append(nombre)

    def agregar_conexion(self, origen, destino, tiempo, linea):
        self.estaciones[origen][destino] = (tiempo, linea)
        self.estaciones[destino][origen] = (tiempo, linea)

    def agregar_transbordo(self, estacion, tiempo=3):
        self.transbordos.add(estacion)

    def cerrar_estacion(self, nombre):
        if nombre not in self.estaciones:
            return {}
        vecinos_eliminados = self.estaciones.pop(nombre)
        for vecino in vecinos_eliminados:
            if vecino in self.estaciones and nombre in self.estaciones[vecino]:
                del self.estaciones[vecino][nombre]
        for linea in self.lineas:
            if nombre in self.lineas[linea]:
                self.lineas[linea].remove(nombre)
        return vecinos_eliminados

    def restaurar_estacion(self, nombre, vecinos, linea_original):
        self.estaciones[nombre] = vecinos
        for vecino, (tiempo, linea) in vecinos.items():
            if vecino in self.estaciones:
                self.estaciones[vecino][nombre] = (tiempo, linea)
        if linea_original in self.lineas:
            self.lineas[linea_original].append(nombre)

    def es_transbordo(self, estacion):
        return estacion in self.transbordos

    def vecinos(self, estacion):
        return self.estaciones.get(estacion, {})

    def existe(self, estacion):
        return estacion in self.estaciones

    def total_estaciones(self):
        return len(self.estaciones)

    def total_conexiones(self):
        return sum(len(v) for v in self.estaciones.values()) // 2

    def estaciones_hub(self):
        grados = [(e, len(v)) for e, v in self.estaciones.items()]
        return sorted(grados, key=lambda x: x[1], reverse=True)

    def verificar_conectividad(self):
        if not self.estaciones:
            return True
        inicio = next(iter(self.estaciones))
        visitados = set()
        cola = [inicio]
        while cola:
            actual = cola.pop(0)
            if actual in visitados:
                continue
            visitados.add(actual)
            for vecino in self.estaciones[actual]:
                if vecino not in visitados:
                    cola.append(vecino)
        return len(visitados) == len(self.estaciones)

    def __repr__(self):
        return f"Grafo Metro Medellin: {self.total_estaciones()} estaciones, {self.total_conexiones()} tramos"


def construir_metro_medellin():
    g = Grafo()

    linea_a = [
        "Niquia","Bello","Madera","Acevedo","Tricentenario","Caribe",
        "Universidad","Hospital","Prado","Parque Berrio","San Antonio",
        "Alpujarra","Exposiciones","Industriales","Poblado","Aguacatala",
        "Ayura","Envigado","Itagui","La Estrella"
    ]
    tiempos_a = [2,2,3,2,2,2,2,2,2,1,2,2,2,3,3,2,2,2,3]
    for e in linea_a:
        g.agregar_estacion(e, "A")
    for i in range(len(linea_a)-1):
        g.agregar_conexion(linea_a[i], linea_a[i+1], tiempos_a[i], "A")

    linea_b = ["San Antonio","Suramericana","Estadio","Floresta","Santa Lucia","Trinidad","San Javier"]
    tiempos_b = [2,2,2,2,2,3]
    for e in linea_b:
        g.agregar_estacion(e, "B")
    for i in range(len(linea_b)-1):
        g.agregar_conexion(linea_b[i], linea_b[i+1], tiempos_b[i], "B")

    linea_k = ["Acevedo","Andalucia","Popular","Santo Domingo"]
    tiempos_k = [4,4,4]
    for e in linea_k:
        g.agregar_estacion(e, "K")
    for i in range(len(linea_k)-1):
        g.agregar_conexion(linea_k[i], linea_k[i+1], tiempos_k[i], "K")

    linea_j = ["San Javier","Juan XXIII","Vallejuelos"]
    tiempos_j = [5,5]
    for e in linea_j:
        g.agregar_estacion(e, "J")
    for i in range(len(linea_j)-1):
        g.agregar_conexion(linea_j[i], linea_j[i+1], tiempos_j[i], "J")

    linea_ta = ["Industriales","Cisneros","Oriente","Miraflores","Alejandro Echavarria","Bicentenario","Buenos Aires"]
    tiempos_ta = [3,3,3,3,3,3]
    for e in linea_ta:
        g.agregar_estacion(e, "T-A")
    for i in range(len(linea_ta)-1):
        g.agregar_conexion(linea_ta[i], linea_ta[i+1], tiempos_ta[i], "T-A")

    g.agregar_transbordo("San Antonio")
    g.agregar_transbordo("Acevedo")
    g.agregar_transbordo("Industriales")
    g.agregar_transbordo("San Javier")

    return g


if __name__ == "__main__":
    metro = construir_metro_medellin()
    print(metro)
    print(f"\nTransbordos: {metro.transbordos}")
    print(f"Red conectada: {metro.verificar_conectividad()}")
    print("\nTop 5 hubs:")
    for e, g in metro.estaciones_hub()[:5]:
        print(f"  {e}: {g} conexiones")
