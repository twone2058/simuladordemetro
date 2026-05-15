# Historial de Prompts - Simulador Metro de Medellin

## Etapa 1 - Definicion del problema

**Objetivo:** Escribir el problema con palabras propias antes de usar la IA.

**Texto del estudiante:**
Muchas personas que usan el metro de Medellin no saben cual es la ruta mas rapida
para llegar de una estacion a otra. Esto puede hacer que pierdan tiempo, se equivoquen
de linea o hagan mas transbordos de los necesarios. Este problema afecta principalmente
a usuarios del transporte publico, turistas y personas que no conocen bien el sistema
de metro. La solucion que imagino es una aplicacion que muestre el mapa del metro y
permita seleccionar una estacion de inicio y una de destino.

**Por que este prompt:** El profesor exige que el estudiante defina el problema
antes de usar la IA. Esta es la version original sin refinamiento.

---

## Etapa 2 - Refinamiento del problema

**Objetivo:** Mejorar la redaccion del problema sin cambiar la intencion original.

**Prompt enviado:**
"Tengo el siguiente problema que quiero resolver como proyecto academico.
Por favor, ayudame a reformularlo de forma mas clara, precisa y estructurada,
sin cambiar la intencion original: [descripcion del estudiante]"

**Que genero la IA:** Reformulacion estructurada con contexto, definicion formal,
actores afectados, solucion propuesta y criterio de exito.

**Que cambio el estudiante:** Se mantuvo la reformulacion sin cambios porque
conservaba la intencion original.

---

## Etapa 3 - Justificacion de la estructura de datos

**Objetivo:** Identificar y justificar la estructura de datos mas adecuada.

**Prompt enviado:**
"Dado el problema del Metro de Medellin, justifica por que un grafo ponderado
no dirigido es la estructura mas adecuada y por que no sirven las alternativas."

**Que genero la IA:** Tabla comparativa de estructuras, justificacion de nodos,
aristas y pesos, decision de grafo no dirigido con lista de adyacencia.

**Que cambio el estudiante:** Se acepto la justificacion completa.

---

## Etapa 4 - Implementacion de grafo.py

**Objetivo:** Crear la clase Grafo con el modelo real del Metro de Medellin.

**Prompt enviado:**
"Implementa en Python la clase Grafo para modelar el Metro de Medellin.
Debe incluir metodos para agregar estaciones, conexiones, transbordos,
cerrar estaciones, verificar conectividad e identificar hubs."

**Que genero la IA:** Clase Grafo completa con lista de adyacencia y
funcion construir_metro_medellin con las 5 lineas reales.

**Que reviso el estudiante:** Se verifico que las estaciones y tiempos
correspondieran a la red real del Metro de Medellin.

---

## Etapa 5 - Implementacion de dijkstra.py

**Objetivo:** Implementar Dijkstra con costo adicional por transbordo.

**Prompt enviado:**
"Implementa Dijkstra para el Metro de Medellin donde los transbordos
tienen un costo adicional de 3 minutos. Debe retornar tiempo total,
ruta e identificar las estaciones de transbordo."

**Que genero la IA:** Dijkstra con heapq, deteccion de cambio de linea
y reconstruccion de ruta con marcado de transbordos.

**Que reviso el estudiante:** Se verifico que el costo de transbordo
se aplicara correctamente solo en estaciones de conexion.

---

## Etapa 6 - Implementacion de bfs.py

**Objetivo:** Implementar BFS para minimizar cambios de linea.

**Prompt enviado:**
"Implementa BFS para encontrar la ruta con el menor numero de cambios
de linea en el Metro de Medellin. El estado debe rastrear la linea actual
para detectar transbordos correctamente."

**Que genero la IA:** BFS con estado (estacion, linea) usando deque,
registro de visitados para evitar ciclos y deteccion de mejor ruta.

**Que reviso el estudiante:** Se verifico que el conteo de transbordos
fuera correcto en rutas con multiples cambios de linea.

---

## Etapa 7 - Implementacion de simulador.py

**Objetivo:** Crear el menu principal que integre todos los modulos.

**Prompt enviado:**
"Crea el menu principal del simulador que integre grafo, dijkstra y bfs.
Debe incluir opciones para ver estaciones, calcular rutas, comparar ambas
rutas, simular cierre de estacion e identificar hubs."

**Que genero la IA:** Menu interactivo con 7 opciones, funcion comparar_rutas
y simulacion de cierre con restauracion automatica de la estacion.

**Que reviso el estudiante:** Se probo cada opcion del menu manualmente.

---

## Etapa 8 - Implementacion de visualizacion.py

**Objetivo:** Generar mapa PNG del metro compatible con Codespaces.

**Prompt enviado:**
"Genera un mapa PNG del Metro de Medellin usando matplotlib con backend Agg
para Codespaces. Cada linea debe tener su color y debe poder resaltar una
ruta calculada en amarillo."

**Que genero la IA:** Mapa con fondo oscuro, colores por linea, marcadores
especiales para transbordos y resaltado de ruta en amarillo punteado.

**Que reviso el estudiante:** Se verifico que el archivo PNG se generara
correctamente sin errores de display en Codespaces.

---

## Etapa 9 - Pruebas

**Objetivo:** Verificar correctitud de los algoritmos con casos de prueba.

**Prompt enviado:**
"Genera pruebas para verificar: total de estaciones, conectividad de la red,
transbordos correctos, cierre y restauracion de estacion, Dijkstra en misma
linea, Dijkstra con transbordo, BFS sin transbordos y estacion inexistente."

**Que genero la IA:** Dos archivos de prueba con 8 casos en total usando
assert para verificacion automatica.

**Que reviso el estudiante:** Se ejecutaron todas las pruebas y se verifico
que todas pasaran correctamente.
