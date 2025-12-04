# Proyecto Copilot - Blog de Grafos

## 📚 Descripción

Blog educativo completo y estructurado sobre **Estructura de Datos: Grafos**. 
Incluye documentación, ejemplos de código, diagramas visuales y referencias rápidas.

## 🎯 Contenido Principal

### 1. **Blog Interactivo** (`blog-grafos/index.html`)
- Introducción a grafos
- Definición formal y componentes
- Tipos de grafos (dirigido, no dirigido, ponderado, etc.)
- 3 formas de representación (matriz, lista, aristas)
- Algoritmos principales (DFS, BFS, Dijkstra, Floyd-Warshall, etc.)
- Aplicaciones en mundo real
- Análisis de complejidad

### 2. **Ejemplos Python** (`blog-grafos/assets/ejemplos.py`)
- Implementación de clase Grafo
- DFS (Búsqueda en Profundidad)
- BFS (Búsqueda en Amplitud)
- Algoritmo de Dijkstra
- Detección de componentes conexas
- Detección de ciclos
- Matriz de adyacencia
- Ejemplos ejecutables listos para correr

### 3. **Diagramas Visuales** (`blog-grafos/assets/diagramas.txt`)
15+ diagramas ASCII mostrando:
- Grafos simples y complejos
- Tipos de grafos
- Búsquedas (DFS, BFS)
- Ciclos y componentes
- Árboles de expansión mínima
- Caminos más cortos

### 4. **Referencia Rápida** (`blog-grafos/assets/referencia_rapida.txt`)
Guía de bolsillo con:
- Definiciones clave
- Complejidades de operaciones
- Resumen de algoritmos
- Propiedades y fórmulas
- Casos de uso vs representación
- Tips y trucos
- Aplicaciones comunes

## 📁 Estructura del Proyecto

```
proyecto-copilot/
├── index.html                     ← Centro de documentación
├── README.md                      ← Este archivo
└── blog-grafos/
    ├── index.html                 ← Blog principal
    ├── README.md                  ← Documentación del blog
    ├── css/
    │   └── styles.css            ← Estilos centralizados
    ├── js/
    │   └── main.js               ← Funcionalidad JavaScript
    ├── assets/
    │   ├── ejemplos.py           ← Código Python
    │   ├── diagramas.txt         ← Diagramas ASCII
    │   └── referencia_rapida.txt ← Guía de referencia
    └── pages/
        └── (Próximas secciones)
```

## 🚀 Cómo Usar

### Opción 1: Abre el Centro de Documentación
```bash
# Abre index.html en tu navegador
start index.html
# O arrastra el archivo a tu navegador
```

### Opción 2: Ve directamente al blog
```bash
# Abre blog-grafos/index.html
start blog-grafos/index.html
```

### Opción 3: Ejecuta los ejemplos Python
```bash
python blog-grafos/assets/ejemplos.py
```

## ✨ Características

✅ **Diseño Moderno**
- Interfaz responsiva y atractiva
- Gradientes y animaciones suaves
- Navegación sticky e interactiva

✅ **Contenido Completo**
- Definiciones formales y conceptos
- Implementaciones prácticas en Python
- Ejemplos visuales con diagramas
- Análisis de complejidad

✅ **Estructura Modular**
- CSS centralizado y reutilizable
- JavaScript funcional y clean
- Fácil de mantener y expandir
- Separación de responsabilidades

✅ **Educativo**
- Explicaciones claras y detalladas
- Tablas comparativas
- Aplicaciones reales
- Código comentado

## 📚 Temas Cubiertos

### Conceptos Fundamentales
- Definición de grafo G = (V, E)
- Vértices, aristas, pesos
- Grado de un vértice

### Tipos de Grafos
- No dirigido vs Dirigido
- Ponderado vs No ponderado
- Conexo vs Desconectado
- Cíclico vs Acíclico
- Completo
- Bipartito

### Representaciones
- Matriz de Adyacencia: O(V²) espacio
- Lista de Adyacencia: O(V + E) espacio
- Lista de Aristas: O(E) espacio

### Algoritmos de Búsqueda
- **DFS**: O(V + E) - Profundidad
- **BFS**: O(V + E) - Amplitud

### Algoritmos de Camino Más Corto
- **Dijkstra**: O((V + E) log V) - Pesos positivos
- **Bellman-Ford**: O(V * E) - Pesos negativos
- **Floyd-Warshall**: O(V³) - Todos los pares

### Algoritmos de MST
- **Prim**: O((V + E) log V)
- **Kruskal**: O(E log E)

### Otros Temas
- Detección de ciclos
- Componentes conexas
- Ordenamiento topológico
- Vértices articulados
- Puentes (bridges)

## 🎓 Aplicaciones Reales

- 📱 **Redes Sociales**: Relaciones entre usuarios
- 🗺️ **GPS/Mapas**: Rutas óptimas, navegación
- 🌐 **Redes de Computadoras**: Conectividad, enrutamiento
- 🧪 **Química**: Estructuras moleculares
- 📋 **Planificación**: Dependencias entre tareas
- 🔍 **Motores de Búsqueda**: PageRank, Web crawling
- 🎮 **Juegos**: Pathfinding, IA
- 🗄️ **Bases de Datos**: Relaciones entre entidades

## 💡 Próximas Expansiones

- [ ] Página de ejercicios interactivos
- [ ] Visualizador interactivo de grafos
- [ ] Tutoriales paso a paso
- [ ] Problemas resueltos de leetcode/hackerrank
- [ ] Animaciones de algoritmos
- [ ] Quiz y evaluaciones
- [ ] Galería de proyectos

## 🛠️ Tecnologías Utilizadas

- **Frontend**: HTML5, CSS3, JavaScript Vanilla
- **Backend**: Python 3
- **Diseño**: Responsive, Mobile-first
- **Estilos**: Gradientes, Animaciones, Transiciones

## 📖 Cómo Estudiar

1. **Inicio**: Lee el blog principal desde el inicio
2. **Conceptos**: Entiende las definiciones y tipos
3. **Representación**: Aprende las 3 formas de representar
4. **Algoritmos**: Estudia DFS, BFS y Dijkstra
5. **Práctica**: Ejecuta el código Python
6. **Visualización**: Revisa los diagramas ASCII
7. **Referencia**: Usa la guía rápida para consultas

## ✅ Checklist de Aprendizaje

- [ ] Entiendo qué es un grafo
- [ ] Conozco los diferentes tipos de grafos
- [ ] Puedo representar un grafo de 3 formas
- [ ] Puedo implementar DFS
- [ ] Puedo implementar BFS
- [ ] Entiendo el algoritmo de Dijkstra
- [ ] Conozco las complejidades de cada operación
- [ ] Puedo identificar aplicaciones reales
- [ ] Puedo detectar ciclos en un grafo
- [ ] Puedo encontrar componentes conexas

## 📝 Notas Importantes

- Todos los ejemplos de Python están probados y funcionan
- Los diagramas ASCII son detallados y fáciles de entender
- Las complejidades están basadas en análisis teórico
- Los colores y estilos son consistentes en todo el sitio
- El código es educativo y está bien comentado

## 🎯 Objetivo

Este blog fue creado para proporcionar una **referencia completa, estructurada y fácil de entender** sobre Grafos - una de las estructuras de datos más importantes en Informática.

---

**Hecho con ❤️ para aprender Estructura de Datos**

*Estructura de Datos 2 | Proyecto Copilot 2025*
