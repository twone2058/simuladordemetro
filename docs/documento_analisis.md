# Documento de Analisis - Simulador Metro de Medellin
**Estructura de Datos — Actividad 13 | Universidad Cooperativa de Colombia 2026**

---

## 4.1 Definicion del Problema

Muchas personas que usan el metro de Medellin no saben cual es la ruta mas rapida
para llegar de una estacion a otra. Esto puede hacer que pierdan tiempo, se equivoquen
de linea o hagan mas transbordos de los necesarios.

Este problema afecta principalmente a usuarios del transporte publico, turistas y
personas que no conocen bien el sistema de metro. El impacto es perdida de tiempo,
confusion y retrasos en sus desplazamientos diarios.

La solucion es una aplicacion que muestre el mapa del metro y permita seleccionar
una estacion de inicio y una de destino. La app calcula automaticamente la ruta mas
rapida, indicando las estaciones por las que debe pasar el usuario, donde debe cambiar
de linea y cuanto tiempo tardara el viaje total.

---

## 4.2 Justificacion de la Estructura de Datos

Se utiliza un grafo ponderado no dirigido con lista de adyacencia.

**Por que un grafo y no otra estructura:**

| Alternativa | Por que NO sirve |
|-------------|-----------------|
| Lista/arreglo | No representa conexiones entre estaciones |
| Arbol | No permite ciclos ni multiples rutas entre nodos |
| Tabla hash | Guarda datos pero no modela relaciones de conectividad |
| Grafo ponderado | Modela exactamente estaciones, conexiones y tiempos |

**Representacion de elementos:**
- Nodo: cada estacion del metro (Niquia, San Antonio, Industriales, etc.)
- Arista: tramo directo entre dos estaciones consecutivas
- Peso: tiempo de recorrido en minutos entre las dos estaciones
- Atributo extra: linea a la que pertenece cada tramo (A, B, K, J, T-A)
- Nodo especial: estaciones de transbordo que conectan dos o mas lineas

**Decisiones de diseno:**
- No dirigido: se puede viajar en ambas direcciones entre estaciones
- Con pesos: el tiempo en minutos es el criterio principal de optimizacion
- Transbordo modelado como costo adicional de 3 minutos en los algoritmos

---

## 4.3 Analisis de Complejidad

| Operacion | Complejidad | Observaciones |
|-----------|-------------|---------------|
| Dijkstra (tiempo minimo) | O((V + E) log V) | V estaciones, E tramos, usa heapq |
| BFS (transbordos minimos) | O(V + E) | Sin pesos, minimiza cambios de linea |
| Cierre de estacion | O(grado(v)) | Elimina nodo y todas sus aristas |
| Re-Dijkstra tras cierre | O((V + E) log V) | Recalcula sobre grafo modificado |
| Identificar hubs | O(V log V) | Ordena estaciones por grado |
| Verificar conectividad | O(V + E) | BFS desde cualquier nodo |

---

## 4.4 Requisitos Funcionales

- RF-01: Visualizar el mapa del metro con lineas de colores y estaciones
- RF-02: Calcular la ruta mas rapida con Dijkstra mostrando tiempo total
- RF-03: Calcular la ruta con menos transbordos con BFS
- RF-04: Mostrar itinerario detallado: linea, estaciones, tiempo por tramo
- RF-05: Simular cierre de estacion y encontrar ruta alternativa
- RF-06: Identificar las estaciones hub con mayor numero de conexiones

---

## 4.5 Requisitos No Funcionales

- RNF-01: El calculo de ruta debe ser instantaneo para redes de hasta 100 estaciones
- RNF-02: Las lineas deben distinguirse por color en la visualizacion
- RNF-03: El itinerario debe indicar claramente donde hay transbordo
- RNF-04: La interfaz debe permitir seleccionar estacion por nombre en el menu

---

## 4.6 Preguntas de Reflexion

**Como modelaste el transbordo en el grafo?**
El transbordo se modelo como un costo adicional de tiempo (3 minutos) que se suma
en los algoritmos cuando detectan un cambio de linea en una estacion de conexion.
No se creo un nodo extra porque habria duplicado las estaciones y complicado
innecesariamente la estructura del grafo.

**Cuando conviene minimizar tiempo vs minimizar transbordos?**
Conviene minimizar tiempo cuando el usuario tiene prisa y prefiere llegar rapido
aunque deba cambiar de linea varias veces. Conviene minimizar transbordos cuando
el usuario prefiere comodidad, viaja con equipaje o no conoce bien el sistema
y quiere menos cambios aunque tarde un poco mas.

**Que pasa con la conectividad si cierras una estacion de transbordo?**
Si se cierra una estacion de transbordo que es punto de articulacion, como San Antonio
o Acevedo, parte de la red puede quedar desconectada. Por ejemplo, cerrar San Antonio
desconectaria la Linea B del resto de la red. El simulador detecta esto con
verificar_conectividad() y alerta al usuario.

**Como cambiaria el modelo si anadieras bus urbano?**
Se agregaria una nueva capa de nodos para las paradas de bus con sus propias aristas
y tiempos. Las conexiones entre metro y bus en puntos de integracion tendrian un
costo de transbordo mayor (por ejemplo 5 minutos) para reflejar el tiempo de espera
adicional. Esto convertiria el grafo en un grafo multimodal.

**Como verificaste que la ruta calculada es realmente la optima?**
Se implementaron pruebas con casos conocidos: Niquia a Bello debe ser 2 minutos
en linea directa, y Niquia a La Estrella debe tener 0 transbordos por ser la misma
linea A. Ademas se comparo Dijkstra contra BFS para verificar consistencia entre
los dos algoritmos en las mismas rutas.

**Que ciudad real inspiro tu diseno?**
El sistema esta basado en el Metro de Medellin, Colombia, con sus lineas reales:
Linea A norte-sur, Linea B occidente, cables K y J, y el Tranvia de Ayacucho T-A.
Las estaciones y tiempos aproximados corresponden al sistema real de la ciudad.
