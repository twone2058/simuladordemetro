# AGENTS.md - Registro de Agentes de IA

## Proyecto: Simulador de Metro de Medellin
## Estudiante: Angel Andres Reina
## Materia: Estructura de Datos - Actividad 13
## Universidad: Universidad Cooperativa de Colombia - 2026

---

## Agente 1: Claude (Anthropic)

**Rol:** Agente de refinamiento y documentacion

**Funcionalidades:**
- Reformular el problema del estudiante con mayor claridad y precision
- Justificar la eleccion de la estructura de datos
- Redactar el documento de analisis (secciones 4.1 a 4.6)
- Generar el historial de prompts organizado por etapas
- Redactar el README.md con instrucciones del proyecto

---

## Agente 2: Claude Code (Anthropic)

**Rol:** Agente de implementacion de codigo

**Funcionalidades:**
- Generar la clase Grafo con el modelo real del Metro de Medellin
- Implementar el algoritmo Dijkstra con costo de transbordo
- Implementar BFS para minimizar cambios de linea
- Crear el simulador con menu interactivo de 7 opciones
- Generar el mapa visual PNG con matplotlib

---

## Agente 3: Claude (Anthropic) - Modulo de pruebas

**Rol:** Agente de verificacion y calidad

**Funcionalidades:**
- Generar casos de prueba automatizados con assert
- Verificar conectividad de la red tras cierre de estaciones
- Validar que Dijkstra y BFS producen resultados consistentes
- Detectar y documentar errores reales durante el desarrollo

---

## Agente 4: Claude (Anthropic) - Modulo de interfaz

**Rol:** Agente de desarrollo frontend

**Funcionalidades:**
- Generar index.html con formulario de seleccion de estaciones
- Generar viewer.html con resultados en 5 tabs interactivos
- Reimplementar Dijkstra y BFS en JavaScript para el navegador
- Disenar la interfaz visual minimalista con colores por linea
