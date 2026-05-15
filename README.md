# Simulador Metro de Medellin
**Estructura de Datos - Actividad 13 | Universidad Cooperativa de Colombia 2026**

## Descripcion
Aplicacion en Python que modela el Metro de Medellin como grafo ponderado.
Calcula la ruta mas rapida (Dijkstra) y la ruta con menos transbordos (BFS).

## Algoritmos implementados
| Algoritmo | Proposito | Complejidad |
|-----------|-----------|-------------|
| Dijkstra  | Ruta mas rapida | O((V + E) log V) |
| BFS       | Menos transbordos | O(V + E) |
| BFS/DFS   | Verificar conectividad | O(V + E) |

## Como ejecutar

### Instalar dependencias
pip install matplotlib

### Ejecutar simulador principal
cd src && python simulador.py

### Ejecutar pruebas
python tests/test_grafo.py
python tests/test_algoritmos.py

### Generar mapa visual
cd src && python visualizacion.py

## Estructura del proyecto
metro-medellin/
├── src/
│   ├── grafo.py         - Estructura del grafo
│   ├── dijkstra.py      - Ruta mas rapida
│   ├── bfs.py           - Menos transbordos
│   ├── simulador.py     - Menu principal
│   └── visualizacion.py - Mapa PNG
├── tests/
│   ├── test_grafo.py
│   └── test_algoritmos.py
├── docs/
├── prompts/
├── README.md
└── AGENTS.md

## Datos del estudiante
- Nombre: Angel Andres Reina
- Universidad: Universidad Cooperativa de Colombia
- Materia: Estructura de Datos
- Docente: Diego Leon Arcila Herrera
- Año: 2026
