# AGENTS.md - Registro de uso de IA

## Herramienta utilizada
- Claude (Anthropic) via claude.ai

## Etapas y decisiones

### Etapa 1 - Definicion del problema
- El estudiante escribio el problema con sus propias palabras
- La IA reformulo el problema manteniendo la intencion original

### Etapa 2 - Justificacion de la estructura de datos
- La IA justifico el uso de grafo ponderado no dirigido
- Se decidio usar lista de adyacencia con tuplas (tiempo, linea)
- Se descartaron arboles y listas por no modelar conexiones multiples

### Etapa 3 - Implementacion de grafo.py
- La IA genero la clase Grafo con todos sus metodos
- El estudiante valido la estructura de estaciones y transbordos

### Etapa 4 - Implementacion de dijkstra.py
- La IA implemento Dijkstra con heapq para optimizar rendimiento
- Se agrego costo adicional de 3 min por transbordo de linea

### Etapa 5 - Implementacion de bfs.py
- La IA implemento BFS rastreando estado (estacion, linea)
- Permite encontrar ruta con minimo numero de cambios de linea

### Etapa 6 - Implementacion de simulador.py
- La IA genero el menu principal integrando todos los modulos
- Incluye simulacion de cierre de estacion y ruta alternativa

### Etapa 7 - Implementacion de visualizacion.py
- La IA genero el mapa PNG con backend Agg para Codespaces
- Cada linea tiene su color y las rutas se resaltan en amarillo

### Etapa 8 - Pruebas
- La IA genero tests de verificacion cruzada entre Dijkstra y BFS
- El estudiante ejecuto y valido cada prueba

## Decisiones clave tomadas con apoyo de la IA
1. Modelar transbordo como costo adicional en arista (no como nodo extra)
2. Usar heapq para optimizar Dijkstra a O((V+E) log V)
3. Usar backend Agg en matplotlib para compatibilidad con Codespaces
4. Guardar estado (estacion, linea) en BFS para detectar cambios de linea
5. Commits por etapa para evidenciar el progreso del desarrollo
